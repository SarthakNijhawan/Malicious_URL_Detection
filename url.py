#!/usr/bin/env python3
"""
@author: vikrant
"""

import random

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def get_tokens(url):
    tokens_by_slash = str(url.encode('utf-8')).split('/')
    all_tokens = []
    for i in tokens_by_slash:
        tokens = str(i).split('-')
        tokens_by_dot = []
        for j in range(0, len(tokens)):
            temp_tokens = str(tokens[j]).split('.')
            tokens_by_dot += temp_tokens
        all_tokens = all_tokens + tokens + tokens_by_dot
    all_tokens = list(set(all_tokens))
    if 'com' in all_tokens:
        all_tokens.remove('com')
    return all_tokens


# def run():
urls_filename = 'final2.csv'
# read data from csv file
urls_data = pd.read_csv(urls_filename, ',', error_bad_lines=False)

urls_data = np.array(urls_data)
random.shuffle(urls_data)

Y = [u[-1] for u in urls_data]
# corpus
urls = [u[0] for u in urls_data]

tfidf_vectorizer = TfidfVectorizer(tokenizer=get_tokens)
X = tfidf_vectorizer.fit_transform(urls)
feature_train, feature_test, label_train, label_test = train_test_split(X, Y, test_size=0.2)
logistic_regression = LogisticRegression()
logistic_regression.fit(feature_train, label_train)
print(logistic_regression.score(feature_test, label_test))


# run()
