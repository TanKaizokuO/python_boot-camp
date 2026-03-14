# 🛠️ Setup Guide — Get Your Environment Ready

Welcome! Follow these steps to set up Python on your machine so you can work through every module of this course.

---

## 1. Install Python

If you don't have Python yet, download it from the official site:

👉 [https://www.python.org/downloads/](https://www.python.org/downloads/)

**Minimum version required:** Python 3.10+

Verify your installation:
```bash
python3 --version
```

---

## 2. Clone or Download This Repo

```bash
git clone https://github.com/your-username/python.git
cd python
```

Or simply download the ZIP from GitHub and unzip it.

---

## 3. Create a Virtual Environment

A virtual environment keeps this course's packages isolated from the rest of your system.

```bash
python3 -m venv .venv
```

**Activate it:**

| Platform | Command |
|---|---|
| Linux / macOS | `source .venv/bin/activate` |
| Windows (CMD) | `.venv\Scripts\activate.bat` |
| Windows (PowerShell) | `.venv\Scripts\Activate.ps1` |

Your terminal prompt will show `(.venv)` when it's active.

---

## 4. Install All Course Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `jupyter` — for running notebooks
- `pandas`, `numpy` — for data science modules
- `pydantic` — for Module 10
- `requests`, `beautifulsoup4` — for web scraping
- `openpyxl` — for Excel data handling
- `Pillow` — for image projects
- `psutil` — for system monitoring scripts

---

## 5. Launch Jupyter Notebooks

```bash
jupyter notebook
```

Your browser will open automatically. Navigate to any `.ipynb` file and start learning!

---

## 6. Running Python Scripts

For modules that use `.py` scripts instead of notebooks:

```bash
python path/to/script.py
```

Example:
```bash
python Basic_Projects/ceaser-cipher.py
```

---

## ✅ You're Ready!

Head back to the [README](./README.md) and start with **Module 00 – Getting Started**.

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| `python3: command not found` | Install Python from python.org |
| `pip: command not found` | Use `python3 -m pip install ...` |
| Jupyter won't open | Make sure venv is active and jupyter is installed |
| Package import errors | Re-run `pip install -r requirements.txt` with venv active |
