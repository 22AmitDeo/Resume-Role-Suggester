import spacy
nlp=spacy.load("en_core_web_sm")
def clean_text(text):
        # Lemmatize, lowercase, and remove stopwords/punctuation from text.
        doc = nlp(text)
        cleaned_tokens = [
            token.lemma_.lower() for token in doc 
            if not token.is_stop and not token.is_punct
        ]
        return " ".join(cleaned_tokens)