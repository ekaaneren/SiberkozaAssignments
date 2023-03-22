"""
A process by which a piece of sensitive data, such as a credit card number,
is replaced by a surrogate value known as a token.
"""

from nltk.tokenize import word_tokenize


def tokenize(t):
    return word_tokenize(t)


def main():
    text = "A guy opens his door and gets shot and you think that of me? No. I am the one who knocks!"
    print(tokenize(text))


main()
