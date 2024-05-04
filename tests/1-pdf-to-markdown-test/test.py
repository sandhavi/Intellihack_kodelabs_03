import PyPDF2
from markdownify import markdownify as md

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            text += page.extract_text()
    return text

def convert_to_markdown(pdf_path, markdown_path):
    text = extract_text_from_pdf(pdf_path)
    markdown_content = md(text)
    with open(markdown_path, 'w') as file:
        file.write(markdown_content)

if __name__ == "__main__":
    pdf_path = "llm-scenario.pdf"   #  PDF file path
    markdown_path = "llm-scenario.pdf" # Markdown output path
    convert_to_markdown(pdf_path, markdown_path)
