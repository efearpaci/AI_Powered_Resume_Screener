import re

def clean_resume(text):
    text = text.replace('\r\n', ' ').replace('\n', ' ')
    text = re.sub(r'\*', '', text)  # Remove bullet points
    text = re.sub(r'[^\w\s,.;:?!-]', '', text)  # Remove unwanted special characters
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Remove non-ASCII characters
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    return text.strip().lower()  # Normalize text to lowercase

