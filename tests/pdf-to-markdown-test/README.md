# PDF to Markdown test - success

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip freeze > requirements.txt
```

## Installation

Download libraries

```bash
pip install PyPDF2 markdownify
```

Install libraries listed in requirements

```bash
pip install -r requirements.txt
```

## Run test

```bash
python3 test.py
```
