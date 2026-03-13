# Python Practice Workspace

This repository is a collection of Python learning notebooks and mini-projects.
It includes:

- Core Python topic notebooks (basics to OOP)
- Automation scripts
- Data handling utilities
- Introductory data science exercises
- A few standalone utility scripts

## Folder Overview

```text
.
|- 1.basics.ipynb
|- 2.intermediate.ipynb
|- 3.comprehension.ipynb
|- 4.generaors.ipynb
|- 5.Decorators.ipynb
|- 6.ErrornLog.ipynb
|- 7.OOPs1.ipynb
|- 8.Inheritance.ipynb
|- 9.OOPs2.ipynb
|- ceaser-cipher.py
|- important.py
|- password-checkerr.py
|- Terminal_Task_Manager.py
|- Automation-Task/
|  |- Auto-Batch-Rename.py
|  |- Auto-File-Organizer.py
|  |- Auto-File-Sorter.py
|  |- System-Resource-Monitor.py
|- Basic-Data-Science-Projects/
|  |- day_01.ipynb
|  |- day_02.py
|  |- day_03.py
|  |- day_04.py
|  |- day_05.py
|- Data-Handling-Project/
|  |- CLI_Contact_Book.py
|  |- CSV-TO-JSON.py
|  |- JSON-Flattener.py
|  |- JSON-to-Excel.py
|  |- Offline-Credential-Manager.py
|  |- OfflineNotesLocker.py
|  |- PersonalMovieTracker.py
|  |- Real-TimeWeatherLogger.py
|  |- StudentMarksAnalyzer.py
|- Scientic_func/
|  |- science.py
```

## Requirements

- Python 3.10+ (recommended)
- Jupyter Notebook/Lab for `.ipynb` files

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install common packages used by notebooks/projects:

```bash
pip install jupyter pandas numpy openpyxl
```

Open notebooks:

```bash
jupyter notebook
```

## Running Scripts

Run any script from the repository root:

```bash
python script_name.py
```

Examples:

```bash
python Terminal_Task_Manager.py
python Data-Handling-Project/CLI_Contact_Book.py
python Automation-Task/Auto-File-Organizer.py
```

## Project Groups

### 1) Core Python Notebooks

- `1.basics.ipynb`: Python fundamentals
- `2.intermediate.ipynb`: Intermediate concepts
- `3.comprehension.ipynb`: List/dict/set comprehensions
- `4.generaors.ipynb`: Generators and iterators
- `5.Decorators.ipynb`: Functions and decorators
- `6.ErrornLog.ipynb`: Error handling and logging basics
- `7.OOPs1.ipynb`: Object-oriented programming intro
- `8.Inheritance.ipynb`: Inheritance patterns
- `9.OOPs2.ipynb`: Advanced OOP exercises

### 2) Standalone Scripts

- `ceaser-cipher.py`: Caesar cipher implementation
- `password-checkerr.py`: Password validation/check utility
- `important.py`: General utility/practice script
- `Terminal_Task_Manager.py`: Terminal-based task manager

### 3) Automation-Task

- `Auto-Batch-Rename.py`: Rename files in bulk
- `Auto-File-Organizer.py`: Organize files by rules/categories
- `Auto-File-Sorter.py`: Sort files into folders
- `System-Resource-Monitor.py`: CPU/RAM/system monitoring

### 4) Basic-Data-Science-Projects

- `day_01.ipynb`: Notebook-based data science practice
- `day_02.py` to `day_05.py`: Daily Python/data analysis exercises

### 5) Data-Handling-Project

- `CLI_Contact_Book.py`: Command-line contact manager
- `CSV-TO-JSON.py`: CSV to JSON conversion
- `JSON-Flattener.py`: Flatten nested JSON objects
- `JSON-to-Excel.py`: Convert JSON data to Excel
- `Offline-Credential-Manager.py`: Local credential manager
- `OfflineNotesLocker.py`: Notes storage/locking utility
- `PersonalMovieTracker.py`: Personal movie tracking app
- `Real-TimeWeatherLogger.py`: Weather logging script
- `StudentMarksAnalyzer.py`: Student marks analysis tool

### 6) Scientic_func

- `science.py`: Science/math helper functions

## Notes

- Some file names include spelling variations (for example, `generaors`, `checkerr`, `Scientic_func`). They are kept as-is to match existing project files.
- `.venv/` and `__pycache__/` are environment/runtime artifacts.

## Suggested Next Improvements

- Add a `requirements.txt` or `pyproject.toml` for reproducible dependency setup.
- Add usage examples and sample input/output for each script.
- Add basic tests for critical utilities.
