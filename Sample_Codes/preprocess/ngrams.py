"""
A sequence of N words.
"""

from nltk.tokenize import word_tokenize
from nltk.util import ngrams


def get_ngrams(t, n):
    return ngrams(word_tokenize(t), n)


def main():
    text = "All those moments will be lost in time, like tears in rain."
    n = get_ngrams(text, 3)
    for i in n:
        print(i)


main()
