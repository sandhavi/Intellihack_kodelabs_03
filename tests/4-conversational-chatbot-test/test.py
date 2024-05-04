import sqlite3
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.output_parsers.rail_parser import GuardrailsOutputParser
from IPython.display import display
import ipywidgets as widgets

os.environ["OPENAI_API_KEY"] = "sk-proj-6TWIQvvPe16mdSOmDORcT3BlbkFJ3JJoAk5FmB6yQvHd297j"

# Function to retrieve text chunks from SQLite database
def retrieve_text_chunks_from_database():
    conn = sqlite3.connect('document.db')
    c = conn.cursor()
    c.execute("SELECT content FROM chunks")
    chunks = c.fetchall()
    conn.close()
    return [chunk[0] for chunk in chunks]

# Function to generate embeddings for text chunks using OpenAI
def generate_embeddings(text_chunks):
    embeddings = OpenAIEmbeddings()
    return [embeddings.embed(chunk) for chunk in text_chunks]

# Function to create a vector database using FAISS
def create_vector_database(embeddings):
    db = FAISS.from_embeddings(embeddings)
    return db

# Function to set up conversational retrieval chain
def setup_conversational_retrieval_chain(vector_database):
    return GuardrailsOutputParser.from_retriever(vector_database)

# Function to handle user queries and display responses
def handle_user_query(query, qa_chain, chat_history):
    result = qa_chain({"question": query, "chat_history": chat_history})
    chat_history.append((query, result['answer']))
    display(widgets.HTML(f'<b>User:</b> {query}'))
    display(widgets.HTML(f'<b><font color="blue">Chatbot:</font></b> {result["answer"]}'))

# Main function to run the chatbot
def run_chatbot():
    # Retrieve text chunks from SQLite database
    text_chunks = retrieve_text_chunks_from_database()

    # Generate embeddings for text chunks
    embeddings = generate_embeddings(text_chunks)

    # Create vector database using FAISS
    vector_database = create_vector_database(embeddings)

    # Set up conversational retrieval chain
    qa_chain = setup_conversational_retrieval_chain(vector_database)

    # Initialize chat history
    chat_history = []

    # Create chatbot interface using IPython widgets
    print("Welcome to the Chatbot! Type 'exit' to stop.")
    input_box = widgets.Text(placeholder='Please enter your question:')
    input_box.on_submit(lambda _: handle_user_query(input_box.value, qa_chain, chat_history))
    display(input_box)

if __name__ == '__main__':
    run_chatbot()
