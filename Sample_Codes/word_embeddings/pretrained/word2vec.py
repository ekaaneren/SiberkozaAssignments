"""
The algorithm uses a neural network model to learn word associations from a large corpus of text.
"""

from nltk.tokenize import sent_tokenize, word_tokenize
import warnings
import gensim
from gensim.models import Word2Vec
from wikipedia import wikipedia


def word2vec(data, min_count, vector_size, window,sg):
    return gensim.models.Word2Vec(data, min_count=min_count, vector_size=vector_size, window=window, sg=sg)


def main():
    warnings.filterwarnings(action='ignore')
    artificial_intelligence = wikipedia.page("Artificial Intelligence").content
    data = []
    for i in sent_tokenize(artificial_intelligence):
        temp = []
        for j in word_tokenize(i):
            temp.append(j.lower())

        data.append(temp)

    model1 = word2vec(data, min_count=1, vector_size=100, window=5, sg=0)

    print("Cosine similarity between 'machine' " +
          "and 'matrix' - CBOW : ",
          model1.wv.similarity('machine', 'matrix'))

    print("Cosine similarity between 'alice' " +
          "and 'machine' - CBOW : ",
          model1.wv.similarity('alice', 'machine'))

    model2 = word2vec(data, min_count=1, vector_size=100, window=3, sg=1)

    print("Cosine similarity between 'machine' " +
          "and 'matrix' - Skip Gram : ",
          model2.wv.similarity('machine', 'matrix'))

    print("Cosine similarity between 'alice' " +
          "and 'machine' - Skip Gram : ",
          model2.wv.similarity('alice', 'machine'))


main()
