import re


def clean_resume(text):
    # Replace line breaks with space
    text = text.replace('\r\n', ' ').replace('\n', ' ')

    # Remove bullet points (such as *)
    text = re.sub(r'\*', '', text)

    # Remove other unwanted special characters
    text = re.sub(r'[^\w\s,.;:?!-]', '', text)  # Keep only letters, numbers, and common punctuation

    # Remove non-ASCII characters like 'â¢' or others
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Keep only ASCII characters

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    return text.strip().lower()  # Convert everything to lowercase for consistency