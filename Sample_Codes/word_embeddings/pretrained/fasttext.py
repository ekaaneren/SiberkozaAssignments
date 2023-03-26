"""
A library for learning of word embeddings and text classification created by Facebook's AI Research (FAIR) lab.
"""

from gensim.models.fasttext import FastText
from nltk.tokenize import sent_tokenize

import re
from nltk.stem import WordNetLemmatizer

import wikipedia
import nltk


def main():
    artificial_intelligence = wikipedia.page("Artificial Intelligence").content

    deep_learning = wikipedia.page("Deep Learning").content
    neural_network = wikipedia.page("Neural Network").content

    artificial_intelligence = sent_tokenize(artificial_intelligence)
    deep_learning = sent_tokenize(deep_learning)
    neural_network = sent_tokenize(neural_network)

    artificial_intelligence.extend(deep_learning)
    artificial_intelligence.extend(neural_network)

    final_corpus = [preprocess_text(sentence) for sentence in artificial_intelligence if sentence.strip() != '']

    word_punctuation_tokenizer = nltk.WordPunctTokenizer()
    tokenized_corpus = [word_punctuation_tokenizer.tokenize(sent) for sent in final_corpus]

    embedding_size = 60
    window_size = 40
    min_word = 5
    down_sampling = 1e-2

    semantically_similar_words = {words: [item[0] for item in fasttext(tokenized_corpus, embedding_size, window_size,
                                                                       min_word, down_sampling).wv.most_similar([words],
                                                                                                                topn=5)]
                                  for words in
                                  ['artificial', 'intelligence', 'machine', 'network', 'recurrent', 'deep']}

    for k, v in semantically_similar_words.items():
        print(k + ":" + str(v))


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


def fasttext(tokenized_corpus, embedding_size, window_size, min_word, down_sampling):
    ft_model = FastText(tokenized_corpus,
                        max_vocab_size=embedding_size,
                        window=window_size,
                        min_count=min_word,
                        sample=down_sampling,
                        sg=1)
    return ft_model


main()
