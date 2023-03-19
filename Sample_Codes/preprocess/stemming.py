"""
Stemming is the process of reducing a word to its stem that affixes to suffixes
and prefixes or to the roots of words known as "lemmas".
"""

from nltk.stem import*


def stem(w):
    ps = PorterStemmer()
    return ps.stem(w)


def main():
    words = ["compute", "computes", "computed", "computation", "computer"]

    for word in words:
        print("word: ", word, "\t stem: ", stem(word))


main()
