"""
A text normalization technique used in Natural Language Processing (NLP),
that switches any kind of  word to its base root mode.
"""

from nltk.stem import WordNetLemmatizer


def lemma(w):
    wnl = WordNetLemmatizer()
    return wnl.lemmatize(w, pos="v")


def main():
    words = ["compute", "computes", "computed", "computation", "computer"]

    for word in words:
        print(word, "\t", lemma(word))


main()
