# Markdown to save in db - complete

## 1. Copy the dataset.

Copy the `llm-scenario.pdf` file from `./2-markdown-to-proper-styling-test` folder to `./3-markdown-to-save-in-db-test/data` folder

```bash
cp ../2-markdown-to-proper-styling-test/llm-scenario.pdf ./data/llm-scenario.pdf
```

## 2. Setup

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Installation

Install libraries listed in requirements

```bash
pip install -r requirements.txt
```

## 4. Run test

```bash
python3 test.py
```
