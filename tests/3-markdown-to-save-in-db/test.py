# This test will be used for setup.py

import os
import sqlite3
from markdown2 import markdown
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import GPT2TokenizerFast

def read_markdown_file(markdown_path):
    # Read Markdown file
    with open(markdown_path, 'r', encoding='utf-8') as f:
        markdown_text = f.read()
    return markdown_text

def count_tokens(text: str) -> int:
    # Initialize tokenizer with a larger maximum sequence length
    tokenizer = GPT2TokenizerFast.from_pretrained("gpt2", max_length=512)
    # Count tokens
    return len(tokenizer.encode(text))

def split_text_into_chunks(text, max_chunk_size=300):
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=max_chunk_size,
        chunk_overlap=100,
        length_function=count_tokens,
    )
    
    # Truncate long sequences to fit within the maximum length
    if count_tokens(text) > max_chunk_size:
        text = text[:max_chunk_size]

    return text_splitter.create_documents([text])

def create_database(chunks):
    # Create SQLite database
    conn = sqlite3.connect('document.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS chunks (
                 id INTEGER PRIMARY KEY,
                 content TEXT)''')
    for chunk in chunks:
        c.execute('INSERT INTO chunks (content) VALUES (?)', (chunk,))
    conn.commit()
    conn.close()

def setup():
    markdown_path = "./output.md"
    
    markdown_text = read_markdown_file(markdown_path) # Read Markdown file

    html_text = markdown(markdown_text) # Convert Markdown to HTML

    chunks = split_text_into_chunks(html_text) # Split HTML into chunks

    create_database(chunks) # Create SQLite database and insert chunks

if __name__ == "__main__":
    setup()
