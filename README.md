# Python Learning and Projects Workspace

This repository is a personal Python practice workspace that combines:

- Concept notebooks (fundamentals through OOP)
- Script-based mini projects
- Automation utilities
- Data handling tools
- Threading and async practice
- Web scraping exercises

It is organized as a learning-first codebase, so file naming and style can vary by exercise.

## Quick Start

1. Create and activate a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install common dependencies used across notebooks and scripts.

```bash
pip install jupyter pandas numpy openpyxl requests beautifulsoup4
```

3. Open notebooks (optional).

```bash
jupyter notebook
```

4. Run scripts from the repository root.

```bash
python path/to/script.py
```

## Workspace Map

### Core Notebooks (Root)

- `1.basics.ipynb` to `9.OOPs2.ipynb`: Progressive Python topics from basics to OOP.
- `graph_paper.ipynb`: Additional notebook experiment/practice file.

### Root Utility Scripts

- `ceaser-cipher.py`: Caesar cipher implementation.
- `password-checkerr.py`: Password checking utility.
- `important.py`: General practice script.
- `Terminal_Task_Manager.py`: Terminal-based task manager utility.

### Automation-Task

Automation and system utility scripts:

- `Auto-Batch-Rename.py`
- `Auto-File-Organizer.py`
- `Auto-File-Sorter.py`
- `System-Resource-Monitor.py`

### Basic-Data-Science-Projects

Early data-science practice files:

- `day_01.ipynb`
- `day_02.py` to `day_05.py`

### Data-Handling-Project

Data conversion and CLI utility scripts:

- `CLI_Contact_Book.py`
- `CSV-TO-JSON.py`
- `JSON-Flattener.py`
- `JSON-to-Excel.py`
- `Offline-Credential-Manager.py`
- `OfflineNotesLocker.py`
- `PersonalMovieTracker.py`
- `Real-TimeWeatherLogger.py`
- `StudentMarksAnalyzer.py`

### Ascynchronous_Python/13_async_python

Async and concurrency basics:

- `01_async_one.py` to `03_async_three.py`: Intro async examples
- `04_thread_async.py`, `05_process_async.py`: Async with threads/processes
- `06_bgworker.py`, `07_daemon.py`, `08_non_daemon.py`: Worker and daemon patterns
- `09_race_condition.py`, `10_deadlock.py`: Concurrency pitfalls

### Thread_n_Concurrency/12_threads_concurrency

Threading and multiprocessing practice:

- `01_threading.py` to `04_gil_multiprocessing.py`
- `05_thread_one.py` to `08_thread_lock.py`
- `09_process_one.py` to `12_process_value.py`

### Web_Scrapping-Projects

Web scraping and web automation scripts:

- `Crypto_Price_Tracker-1.py` to `Crypto_Price_Tracker-4.py`
- `Download_Cover-Images-Using-wget.py`
- `SPECIAL-Download-Cover-Images.py`
- `Hacker-News_Top_Posts_Scraper.py`
- `Quote_of_the_Day_Image_Maker.py`
- `Scrap_wiki_Headings.py`
- `Scrape-Books.py`

### Scientic_func

- `science.py`: Basic scientific helper functions.

## Common Commands

Run a root-level script:

```bash
python Terminal_Task_Manager.py
```

Run an async practice script:

```bash
python Ascynchronous_Python/13_async_python/01_async_one.py
```

Run a threading practice script:

```bash
python Thread_n_Concurrency/12_threads_concurrency/01_threading.py
```

Run a data-handling script:

```bash
python Data-Handling-Project/CSV-TO-JSON.py
```

## Notes

- Some names intentionally keep original spelling from practice files, such as `generaors`, `password-checkerr`, `Scientic_func`, and `Web_Scrapping-Projects`.
- `__pycache__/` folders are generated automatically by Python.
- `__MACOSX/` directories appear to be archive artifacts and can usually be ignored.

## Suggested Next Improvements

- Add a `requirements.txt` to pin dependencies.
- Add example input/output for each project script.
- Add lightweight tests for reusable utilities.
