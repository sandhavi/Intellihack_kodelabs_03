# Create Conversational chatbot - incomplete

## 1. Copy database

Copy the `document.db` file from `./3-markdown-to-save-in-db-test` folder to `./4-conversational-chatbot-test` folder

```bash
cp ../3-markdown-to-save-in-db-test/document.db ./document.db
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
pip install ipython
pip install ipywidgets
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
