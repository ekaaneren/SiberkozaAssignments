"""
The process of removing or transforming certain parts of the text so
that the text becomes more easily understandable for NLP models that are learning the text
"""
import re
from nltk.corpus import stopwords

stop = stopwords.words('english')


def clean(t):
    t = t.lower()
    t = re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", t)
    t = " ".join([word for word in t.split() if word not in stop])
    return t


def main():
    text = "hey amazon - my package never arrived" \
           " https://www.amazon.com/gp/css/order-history?ref_=nav_orders_first please fix asap!"
    text = clean(text)
    print(text)


main()
