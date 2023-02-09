import re
from nltk.corpus import stopwords
import string

t = str.maketrans(dict.fromkeys(string.punctuation))

def clean_text(text: str) -> str:
  # Remove stop words
  stop_words = set(stopwords.words('english'))
  text = " ".join(list(set(text.lower().split()) - stop_words))

  # Remove special characters
  text  = text.translate(t)

  # Remove extra spaces
  text = re.sub(' +', ' ', text)

  return text