"""
A numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus.
"""

from sklearn.feature_extraction.text import TfidfVectorizer


def tf_idf(doc):
    tfidf = TfidfVectorizer()
    return {"result": tfidf.fit_transform(doc), "vocab": tfidf.vocabulary_}


def main():
    d = ["Star Wars: Clone Wars", "Star Trek: The Next Generation"]
    tfidf_dic = tf_idf(d)
    print(tfidf_dic["vocab"], tfidf_dic["result"],  sep="\n\n")


main()
