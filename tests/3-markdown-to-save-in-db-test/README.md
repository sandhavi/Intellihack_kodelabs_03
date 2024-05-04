# Markdown to save in db - complete

## 1. Copy the dataset.

Copy the `output.md` file from `./2-markdown-to-proper-styling-test` folder to `./3-markdown-to-save-in-db-test` folder

```bash
cp ../2-markdown-to-proper-styling-test/output.md ./output.md
```

## 2. Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
```

## 3. Installation

Download libraries

```bash
pip install transformers
pip install markdown2
pip install langchain
```

Install libraries listed in requirements

```bash
pip install -r requirements.txt
```

## 4. Run test

```bash
python3 test.py
```
