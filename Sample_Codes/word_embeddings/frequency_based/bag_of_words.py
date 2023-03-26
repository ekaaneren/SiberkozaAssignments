"""
A simplifying representation used in natural language processing and
information retrieval (IR). In this model,
a text (such as a sentence or a document) is represented as the bag (multiset) of its words,
disregarding grammar and even word order but keeping multiplicity.
"""

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


def bag_of_words(li):
    count_vec = CountVectorizer(ngram_range=(1, 1), stop_words='english')
    vec = count_vec.fit_transform(li)
    return pd.DataFrame(vec.toarray(), columns=count_vec.get_feature_names_out())


def main():
    sentence_1 = "This is a good job. I feel good about it."
    sentence_2 = "This is not good at all."
    li = [sentence_1, sentence_2]
    df = bag_of_words(li)
    print(df)


main()
