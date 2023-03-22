"""
A set of commonly used words in any language.
For example, in English, “the”, “is” and “and”, would easily qualify as stop words.
"""

from nltk.corpus import stopwords

stop = stopwords.words('english')


def delete_stopwords(t):
    t = " ".join([word for word in t.split() if word not in stop])
    return t


def main():
    text = "I am a man who try to delete all stopwords from this sentence"
    text = delete_stopwords(text)
    print(text)


main()
