"""
A group of bits among which the legal combinations of values are only those with a single high (1) bit and
all the others low (0).
"""

import numpy as np


def one_hot(sentences):

    token_index = {}
    counter = 0
    max_length = 0

    for sample in sentences:
        for considered_word in sample.split():
            if considered_word not in token_index:
                token_index.update({considered_word: counter + 1})
                counter = counter + 1
        max_length = max(max_length, len(sample.split()))

    results = np.zeros(shape=(len(sentences), max_length, max(token_index.values()) + 1))

    for i, sample in enumerate(sentences):
        for j, considered_word in list(enumerate(sample.split())):
            index = token_index.get(considered_word)
            results[i, j, index] = 1.

    return results


def main():
    sentences = {'Jupiter has 79 known moons .', 'Neptune has 14 confirmed moons !', "moons"}
    print(one_hot(sentences))


main()
