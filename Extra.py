import yaml


# Load config from a YAML file in your DATA_DIR
def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


# Example usage:
config = load_config(f"{DATA_DIR}/NF-UNSW-NB15-v3.yaml")


## 🧩 4. Prepare Dataset

# The dataset loader class is included below. It converts a CSV into PyG `Data` objects and caches them under the `DATA_DIR/pyg_graph_data` folder. Place the CSV named `<dataset>.csv` in the corresponding dataset subfolder inside your `DATA_DIR`. For example, if you use `NF-UNSW-NB15-v3`, upload the CSV to `drive/MyDrive/GATE_data/NF-UNSW-NB15-v3/NF-UNSW-NB15-v3.csv`.

# --- begin dataset code ---
import os
import pickle
import shutil

import numpy as np
import pandas as pd
import torch
import torch_geometric
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset as TorchDataset
from torch_geometric.data import Data

torch.serialization.add_safe_globals(
    [
        torch_geometric.data.data.DataEdgeAttr,
        torch_geometric.data.data.DataTensorAttr,
        torch_geometric.data.storage.GlobalStorage,
    ]
)


def collate_fn(batch):
    sequences, masks = zip(*batch, strict=False)
    sequences_padded = pad_sequence(sequences, batch_first=True, padding_value=0)
    masks_padded = pad_sequence(masks, batch_first=True, padding_value=0)
    return sequences_padded, masks_padded


class SequentialDataset(TorchDataset):
    def __init__(self, data, window, device, step=None):
        self.data = data
        self.window = window
        self.device = device
        if step is None:
            self.step = window
        else:
            self.step = step

    def __getitem__(self, index):
        start_idx = index * self.step
        end_idx = min(start_idx + self.window, len(self.data))
        x = self.data[start_idx:end_idx].to(self.device)
        mask = torch.ones_like(x, dtype=torch.bool).to(self.device)
        return x, mask

    def __len__(self):
        return max(0, (len(self.data) - 1) // self.step + 1)


class NetFlowDataset:
    def __init__(
        self,
        name,
        data_dir,
        force_reload=False,
        fraction=None,
        data_type="benign",
        seed=42,
    ):
        self.name = name
        self.data_dir = data_dir
        self.fraction = fraction
        self.data_type = data_type
        self.seed = seed

        graph_dir = os.path.join(data_dir, "pyg_graph_data")
        if fraction is not None:
            assert 0 < fraction < 1
            fraction_str = str(fraction).replace(".", "_")
            self.processed_dir = os.path.join(graph_dir, f"{name}_{fraction_str}")
        else:
            self.processed_dir = os.path.join(graph_dir, name)

        self.raw_dir = os.path.join(data_dir, name)

        if force_reload and os.path.exists(self.processed_dir):
            print(
                f"Force reload: Removing existing processed data at {self.processed_dir}"
            )
            shutil.rmtree(self.processed_dir)

            scaler_path = os.path.join("scalers", f"scaler_{self.name}.pkl")
            if os.path.exists(scaler_path):
                print(f"Removing old scaler: {scaler_path}")
                os.remove(scaler_path)

        if self._needs_processing():
            seed_file = os.path.join(self.processed_dir, ".seed")
            if os.path.exists(seed_file):
                with open(seed_file) as f:
                    cached_seed = int(f.read().strip())
                if cached_seed != self.seed:
                    print(
                        f"Warning: Cached data was created with seed={cached_seed}, but current seed={self.seed}"
                    )
                    print(
                        "Run with --reload_dataset to recreate data with the new seed"
                    )

            self._process()
        else:
            seed_file = os.path.join(self.processed_dir, ".seed")
            if os.path.exists(seed_file):
                with open(seed_file) as f:
                    cached_seed = int(f.read().strip())
                if cached_seed != self.seed:
                    print(
                        f"Warning: Cached data was created with seed={cached_seed}, but current seed={self.seed}"
                    )
                    print(
                        "Run with --reload_dataset to recreate data with the new seed"
                    )

        self.train_graph = torch.load(os.path.join(self.processed_dir, "train.pt"))[0]
        self.val_graph = torch.load(os.path.join(self.processed_dir, "val.pt"))[0]
        self.test_graph = torch.load(os.path.join(self.processed_dir, "test.pt"))[0]

    def _needs_processing(self):
        if not os.path.exists(self.processed_dir):
            return True

        required_files = ["train.pt", "val.pt", "test.pt"]
        for filename in required_files:
            if not os.path.exists(os.path.join(self.processed_dir, filename)):
                return True

        return False

    def _process(self):
        print(f"Processing dataset {self.name}...")

        os.makedirs(self.processed_dir, exist_ok=True)

        df = pd.read_csv(os.path.join(self.raw_dir, f"{self.name}.csv"))

        if self.fraction is not None:
            df = df.groupby(by="Attack").sample(
                frac=self.fraction, random_state=self.seed
            )

        x = df.drop(columns=["Attack", "Label"])
        y = df[["Attack", "Label"]]

        x = x.replace([np.inf, -np.inf], np.nan)
        x = x.fillna(0)

        if "v3" in self.name:
            edge_features = [
                col
                for col in x.columns
                if col
                not in [
                    "IPV4_SRC_ADDR",
                    "IPV4_DST_ADDR",
                    "FLOW_END_MILLISECONDS",
                    "FLOW_START_MILLISECONDS",
                ]
            ]
        else:
            edge_features = [
                col
                for col in x.columns
                if col not in ["IPV4_SRC_ADDR", "IPV4_DST_ADDR"]
            ]

        df = pd.concat([x, y], axis=1)

        df_train, df_val_test = train_test_split(
            df, test_size=0.2, random_state=self.seed, stratify=y["Attack"]
        )

        if self.data_type == "benign":
            df_train = df_train[df_train["Label"] == 0]

        scaler_path = os.path.join("scalers", f"scaler_{self.name}.pkl")
        if os.path.exists(scaler_path):
            try:
                with open(scaler_path, "rb") as f:
                    scaler = pickle.load(f)
            except Exception as e:
                print(f"Failed to load scaler: {e}. Creating new one.")
                scaler = MinMaxScaler()
                scaler.fit(df_train[edge_features])
        else:
            scaler = MinMaxScaler()
            scaler.fit(df_train[edge_features])
            os.makedirs(os.path.dirname(scaler_path), exist_ok=True)
            with open(scaler_path, "wb") as f:
                pickle.dump(scaler, f)

        df_train[edge_features] = scaler.transform(df_train[edge_features])
        df_val_test_scaled = scaler.transform(df_val_test[edge_features])
        df_val_test[edge_features] = np.clip(df_val_test_scaled, -10, 10)

        df_val, df_test = train_test_split(
            df_val_test,
            test_size=0.5,
            random_state=self.seed,
            stratify=df_val_test["Attack"],
        )

        if "v3" in self.name:
            df_train = df_train.sort_values(by="FLOW_START_MILLISECONDS")
            df_val = df_val.sort_values(by="FLOW_START_MILLISECONDS")
            df_test = df_test.sort_values(by="FLOW_START_MILLISECONDS")

        unique_nodes = pd.concat(
            [
                df_train["IPV4_SRC_ADDR"],
                df_train["IPV4_DST_ADDR"],
                df_val["IPV4_SRC_ADDR"],
                df_val["IPV4_DST_ADDR"],
                df_test["IPV4_SRC_ADDR"],
                df_test["IPV4_DST_ADDR"],
            ]
        ).unique()
        node_map = {node: i for i, node in enumerate(unique_nodes)}
        num_nodes = len(node_map)

        datasets = {"train": df_train, "val": df_val, "test": df_test}

        for split_name, df_split in datasets.items():
            src_nodes = np.array([node_map[ip] for ip in df_split["IPV4_SRC_ADDR"]])
            dst_nodes = np.array([node_map[ip] for ip in df_split["IPV4_DST_ADDR"]])
            edge_index = torch.tensor(
                np.array([src_nodes, dst_nodes]), dtype=torch.long
            )
            edge_attr = torch.tensor(df_split[edge_features].values, dtype=torch.float)
            edge_labels = torch.tensor(df_split["Label"].values, dtype=torch.long)
            x = torch.ones(num_nodes, edge_attr.shape[1], dtype=torch.float)
            data = Data(
                x=x,
                edge_index=edge_index,
                edge_attr=edge_attr,
                edge_labels=edge_labels,
                num_nodes=num_nodes,
            )

            torch.save([data], os.path.join(self.processed_dir, f"{split_name}.pt"))

        seed_file = os.path.join(self.processed_dir, ".seed")
        with open(seed_file, "w") as f:
            f.write(str(self.seed))

        print("Done!")

    def __len__(self):
        return 3

    @property
    def num_node_features(self):
        return self.train_graph.x.shape[1]

    @property
    def num_edge_features(self):
        return self.train_graph.edge_attr.shape[1]

    @property
    def num_nodes(self):
        return self.train_graph.num_nodes


# --- end dataset code ---

# create an instance
dataset = NetFlowDataset(name="NF-UNSW-NB15-v3", data_dir=DATA_DIR)
print("Loaded graphs with", dataset.num_edge_features, "edge features")


def calculate_errors(outputs, batch, mask):
    # mask shape: (B, T, F), returns one scalar per window (B,)
    squared_errors = ((outputs - batch) ** 2) * mask
    valid_counts = mask.sum(dim=(1, 2)).clamp(min=1)
    mean_errors = squared_errors.sum(dim=(1, 2)) / valid_counts
    return torch.nan_to_num(mean_errors, nan=0.0, posinf=1e6, neginf=-1e6)


def validate(model, val_loader, ae_batch_size, window_size, device):
    criterion = nn.MSELoss(reduction="none")
    model.eval()
    errors = []
    labels = []
    total_val_loss = 0.0

    with torch.inference_mode():
        for batch in val_loader:
            batch.batch_edge_couples = batch.edge_label_index.t()
            batch = batch.to(device)

            val_emb = model.encoder(
                batch.edge_index,
                batch.edge_attr,
                batch.batch_edge_couples,
                batch.num_nodes,
            )
            batch_edge_labels = batch.edge_label.cpu()

            ae_val_loader = DataLoader(
                SequentialDataset(
                    val_emb, window=window_size, step=window_size, device=device
                ),
                batch_size=ae_batch_size,
                collate_fn=collate_fn,
            )

            accumulated_loss = torch.tensor(0.0, device=device)
            seq_count = 0
            seq_idx = 0  # window offset, reset per graph batch

            for ae_batch, mask in ae_val_loader:
                outputs = model.transformer(ae_batch, mask)

                loss = torch.sum(criterion(outputs, ae_batch) * mask) / torch.sum(mask)
                accumulated_loss += loss
                seq_count += 1

                batch_errors = calculate_errors(outputs, ae_batch, mask)
                errors.append(batch_errors.cpu())

                # ae_batch may contain multiple windows — label each one
                for i in range(ae_batch.size(0)):
                    start = (seq_idx + i) * window_size
                    end = min(start + window_size, len(batch_edge_labels))
                    if end > start:
                        labels.append(batch_edge_labels[start:end].max().unsqueeze(0))

                seq_idx += ae_batch.size(0)

            if seq_count > 0:
                total_val_loss += (accumulated_loss / seq_count).item()

    total_val_loss /= len(val_loader)
    errors = torch.cat(errors) if errors else torch.tensor([])
    labels = torch.cat(labels) if labels else torch.tensor([])
    return total_val_loss, errors, labels


def test(model, test_loader, ae_batch_size, window_size, device, threshold):
    torch.cuda.synchronize() if device == "cuda" else None
    start_time = time.perf_counter()
    model.eval()
    errors = []
    labels = []

    with torch.inference_mode():
        for batch in test_loader:
            batch.batch_edge_couples = batch.edge_label_index.t()
            batch = batch.to(device)

            test_emb = model.encoder(
                batch.edge_index,
                batch.edge_attr,
                batch.batch_edge_couples,
                batch.num_nodes,
            )
            batch_edge_labels = batch.edge_label.cpu()

            ae_test_loader = DataLoader(
                SequentialDataset(
                    test_emb, window=window_size, step=window_size, device=device
                ),
                batch_size=ae_batch_size,
                collate_fn=collate_fn,
            )

            seq_idx = 0  # reset per graph batch

            for ae_batch, mask in ae_test_loader:
                outputs = model.transformer(ae_batch, mask)

                batch_errors = calculate_errors(outputs, ae_batch, mask)
                errors.append(batch_errors.cpu())

                # ae_batch may contain multiple windows — label each one
                for i in range(ae_batch.size(0)):
                    start = (seq_idx + i) * window_size
                    end = min(start + window_size, len(batch_edge_labels))
                    if end > start:
                        labels.append(batch_edge_labels[start:end].max().unsqueeze(0))

                seq_idx += ae_batch.size(
                    0
                )  # advance by actual number of windows processed

    errors = torch.cat(errors) if errors else torch.tensor([])
    labels = torch.cat(labels) if labels else torch.tensor([])

    test_pred = (
        (errors > threshold).int()
        if threshold is not None
        else (errors > errors.mean()).int()
    )
    if threshold is None:
        print("No threshold provided, using mean of errors for prediction.")

    torch.cuda.synchronize() if device == "cuda" else None
    prediction_time = time.perf_counter() - start_time

    f1 = f1_score(labels, test_pred, average="macro", zero_division=0)
    pr_auc = average_precision_score(labels, errors)
    return f1, pr_auc, errors, labels, prediction_time


# train loop
model, threshold = train_encoder(
    model,
    config["window_size"],
    config["step_percent"],
    config["ae_batch_size"],
    train_loader,
    val_loader,
    test_loader,
    0,
    config["num_epochs"],
    optimizer,
    patience=config["patience"],
    checkpoint="checkpoint.pt",
    device=device,
)


# final evaluation
print("Evaluating on test set...")
test_f1, test_pr_auc, errors, test_labels, prediction_time = test(
    model,
    test_loader,
    config["ae_batch_size"],
    config["window_size"],
    device,
    threshold=threshold,
)
print(f"Test macro F1-score: {test_f1:.4f}")
print(f"Test PR-AUC: {test_pr_auc:.4f}")
print(f"Prediction time: {prediction_time:.4f} s")
