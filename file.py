import pandas as pd
import re

# Load the CSV
df = pd.read_csv('cases.csv')

def clean_text(text):
    # Remove line breaks and hyphenation artifacts
    text = re.sub(r'-\n', '', text)  # Remove hyphen + newline
    text = re.sub(r'\n', ' ', text)  # Replace newlines with space
    text = re.sub(r'\s+', ' ', text) # Collapse whitespace
    return text.strip()

def extract_meaningful_sentence(text):
    # Split into sentences (simple split on period, can be improved)
    sentences = re.split(r'\.\s+', text)
    # Heuristic: pick the first long sentence, or one containing key words
    for s in sentences:
        if len(s.split()) > 15 and any(k in s.lower() for k in ['issue', 'question', 'held', 'conclusion', 'main point']):
            return s.strip()
    # Fallback: return the first sentence
    return sentences[0].strip() if sentences else ''

# Apply cleaning and extraction
df['clean_text'] = df['text'].apply(clean_text)
df['meaningful_sentence'] = df['clean_text'].apply(extract_meaningful_sentence)

# Output: id and meaningful_sentence
result = df[['id', 'meaningful_sentence']]
result.to_csv('cases_meaningful_sentences.csv', index=False)
