# Setup Guide

Follow this guide to prepare your machine for the full course.

## 1. Install Python

- Download Python from the official website: https://www.python.org/downloads/
- Recommended version: Python 3.10 or newer.

Check installation:

```bash
python3 --version
```

If `python3` is not available on your system, try:

```bash
python --version
```

## 2. Open This Course Folder

In terminal, move into this project:

```bash
cd /path/to/python
```

## 3. Create a Virtual Environment

```bash
python3 -m venv .venv
```

Activate it:

- Linux/macOS:

```bash
source .venv/bin/activate
```

- Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

- Windows CMD:

```cmd
.venv\Scripts\activate.bat
```

When active, your prompt usually shows `(.venv)`.

## 4. Upgrade pip (Recommended)

```bash
python -m pip install --upgrade pip
```

## 5. Install Required Packages

```bash
pip install -r requirements.txt
```

Installed packages cover notebooks, data processing, scraping, validation, imaging, and monitoring.

## 6. Open and Run Notebooks

Start Jupyter:

```bash
jupyter notebook
```

Then open notebooks in this order:

1. `00_intro/getting_started.ipynb`
2. `1.basics.ipynb`
3. Continue by syllabus order in `SYLLABUS.md`

## 7. Run Script-Based Modules

Use this pattern:

```bash
python path/to/file.py
```

Examples:

```bash
python Basic_Projects/Terminal_Task_Manager.py
python Data-Handling-Project/CSV-TO-JSON.py
python Web_Scrapping-Projects/Scrape-Books.py
```

## Troubleshooting

| Problem                          | Fix                                                                  |
| -------------------------------- | -------------------------------------------------------------------- |
| `python3: command not found`     | Reinstall Python and ensure PATH is enabled during installation      |
| `pip: command not found`         | Run installs with `python -m pip ...`                                |
| `ModuleNotFoundError`            | Activate venv, then reinstall with `pip install -r requirements.txt` |
| Jupyter not opening              | Run `python -m pip install jupyter` and start again                  |
| Permission errors on Linux/macOS | Avoid system Python writes; use the local venv                       |

## Done

You can now start from [README.md](./README.md) and follow [SYLLABUS.md](./SYLLABUS.md).
