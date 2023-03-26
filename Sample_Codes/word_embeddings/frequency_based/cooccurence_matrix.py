"""
A square matrix where it depicts the co-occurrence of two terms in a context.
"""

import numpy as np
import pandas as pd


def build_co_occurrence_matrix(all_tokens, window_size):
    unique = set()
    for sentence in all_tokens:
        for token in sentence:
            unique.add(token)
    word_dict = {word: np.zeros(shape=(len(unique))) for word in unique}
    word_list = list(word_dict.keys())
    for sentence in all_tokens:
        for index, token in enumerate(sentence):
            i = max(0, index - window_size)
            j = min(len(sentence) - 1, index + window_size)
            search = [sentence[idx] for idx in range(i, j + 1)]
            search.remove(token)
            for neighbor in search:
                nei_idx = word_list.index(neighbor)
                word_dict[token][nei_idx] += 1
    return word_dict


def main():
    sample = [['I', 'love', 'AI'],['I', 'love', 'deep', 'learning'], ['I', 'enjoy', 'learning']]
    co_oc = build_co_occurrence_matrix(sample, 1)
    print(pd.DataFrame(co_oc, index=co_oc.keys()).astype('int'))


main()
