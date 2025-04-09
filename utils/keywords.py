import spacy

nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):

    doc = nlp(text)
    keywords = {chunk.text.lower().strip() for chunk in doc.noun_chunks if len(chunk.text) > 1}
    return keywords