import re
import pandas as pd
import numpy as np
import string
import nltk
from nltk import tokenize

stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords.remove('não')

def translate(word):
    repl = str.maketrans(
        "áéúíóâêîôûçãõäëöüàèìòù",
        "aeuioaeioucaoaeouaeiou"
        )
    return word.translate(repl)

def strip_punctuations(s):
    punctuations=r'''!()[]{};:'"\,<>./@#$%^&*_'''

    regex = re.compile('[%s]' % re.escape(punctuations))
    return regex.sub('', s)

def remove_stopwords(x):
    x = ' '.join([word for word in x.split() if word not in stopwords])
    return x

def transform_text(X):
    X = [str(i) for i in X]
    X = [i.replace('\n', ' ') for i in X]
    X = [i.replace('\t', ' ') for i in X]
    X = [i.lower() for i in X]
    X = [remove_stopwords(i) for i in X]
    X = [translate(i) for i in X]
    X = [strip_punctuations(i) for i in X]
    return X