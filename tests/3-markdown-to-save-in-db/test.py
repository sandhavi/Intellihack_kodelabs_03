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

def chunk_markdown_file(input_file, output_dir, chunk_size=512):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Read the Markdown file
    with open(input_file, 'r', encoding='utf-8') as f:
        markdown_text = f.read()

    # Split the Markdown content into chunks
    chunks = [markdown_text[i:i+chunk_size] for i in range(0, len(markdown_text), chunk_size)]

    # Write each chunk to a separate file in the output directory
    for i, chunk in enumerate(chunks):
        output_file = os.path.join(output_dir, f'chunk_{i}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(chunk)

    return chunks

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
        content_str = str(chunk)
        c.execute('INSERT INTO chunks (content) VALUES (?)', (content_str,))
    conn.commit()
    conn.close()

def setup():
    markdown_path = "./output.md"
    
    # Chunk the Markdown file
    output_dir = 'chunks'
    chunks = chunk_markdown_file(markdown_path, output_dir)

    # Process each chunk
    for chunk in chunks:
        # Split HTML into smaller chunks
        smaller_chunks = split_text_into_chunks(chunk)

        # Insert smaller chunks into the database
        create_database(smaller_chunks)

if __name__ == "__main__":
    setup()
