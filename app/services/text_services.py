import re
from app.model_loader import text_model

def preprocess_text(text):
    # Lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)

    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()

    return text


def analyze_text(text):
    clean_text = preprocess_text(text)

    pred = text_model.predict([clean_text])[0]

    return {
        "prediction": "Fake" if pred == 1 else "Real"
    }