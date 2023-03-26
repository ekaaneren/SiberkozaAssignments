import pandas as pd
import nltk
import re
from nltk.stem import WordNetLemmatizer
from gensim.corpora import Dictionary
import gensim

df = pd.read_csv(r'C:\Users\KAAN EREN\articles1.csv')
df = df.sample(n=8000)
data = df["content"]


def preprocess_text(document):
    stop = set(nltk.corpus.stopwords.words('english'))
    stemmer = WordNetLemmatizer()
    document = re.sub(r'\W', ' ', str(document))
    document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
    document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
    document = re.sub(r'\s+', ' ', document, flags=re.I)
    document = re.sub(r'^b\s+', '', document)
    document = document.lower()
    tokens = document.split()
    tokens = [stemmer.lemmatize(word) for word in tokens]
    tokens = [word for word in tokens if word not in stop]
    tokens = [word for word in tokens if len(word) > 3]

    preprocessed_text = ' '.join(tokens)

    return preprocessed_text


clean_data = data.apply(preprocess_text)
clean_data_token = clean_data.apply(lambda x: x.split())

dic = Dictionary(clean_data_token)
dic.filter_extremes(no_below=1, no_above=0.7)

X = [dic.doc2bow(i) for i in clean_data_token]

lda = gensim.models.ldamodel.LdaModel(corpus=X, id2word=dic, num_topics=15, passes=10)

subjects = lda.print_topics(num_words=8)

for i in subjects:
    print(i)
    