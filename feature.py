from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

import re
import nltk

def get_all_query(title, author, text):
    total= title + author + text
    total = [total]
    return total

def remove_punctuation_stopwords_lemma(sentence):
    filter_sentence = ''
    lemmatizer=WordNetLemmatizer()
    sentence = re.sub(r'[^\w\s]','',sentence)
    words = nltk.word_tokenize(sentence) #tokenization
    words = [w for w in words if not w in stop_words]
    for word in words:
        filter_sentence = filter_sentence + ' ' + str(lemmatizer.lemmatize(word)).lower()
    return filter_sentence
