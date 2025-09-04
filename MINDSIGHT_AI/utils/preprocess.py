import re

# Define a small custom list of stopwords (expand if needed)
STOPWORDS = {
    "is", "are", "am", "the", "a", "an", "i", "you", "he", "she", "it",
    "we", "they", "me", "my", "your", "our", "this", "that", "was", "were",
    "to", "of", "and", "in", "on", "for", "with", "have", "has", "had"
}

# Basic lemmatizer: only handles plurals for simplicity
def lemmatize_word(word):
    if word.endswith('ies'):
        return word[:-3] + 'y'
    elif word.endswith('s') and not word.endswith('ss'):
        return word[:-1]
    else:
        return word

# Full clean text function
def clean_text(text):
    # Lowercase
    text = text.lower()

    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize (split by space)
    words = text.split()

    # Remove stopwords and lemmatize
    cleaned = [lemmatize_word(word) for word in words if word not in STOPWORDS]

    return ' '.join(cleaned)
