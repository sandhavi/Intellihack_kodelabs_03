# Create Conversational chatbot - complete

## 1. Copy database

Copy the `data` folder from `./3-markdown-to-save-in-db-test` folder to `./4-conversational-chatbot-test` folder

```bash
cp -r ../3-markdown-to-save-in-db-test/data ./data
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
python3 chatbot.py "I am 18 years old. Can I apply for a student loan? If so what do i need for that?"
```
