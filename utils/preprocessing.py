import re


def clean_resume(text):
    # Replace line breaks (\r\n, \n) with space
    text = text.replace('\r\n', ' ').replace('\n', ' ')

    # Remove bullet points (such as *)
    text = re.sub(r'\*', '', text)

    # Remove other unwanted special characters (keeping common punctuation)
    text = re.sub(r'[^\w\s,.;:?!-]', '', text)

    # Remove non-ASCII characters like 'â¢' or others
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)

    # Replace multiple spaces with a single space
    text = re.sub(r'\s+', ' ', text)

    return text.strip().lower()  # Convert everything to lowercase for consistency

