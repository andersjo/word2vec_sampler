from numpy import random


def sample_word2vec(sentence, window=5):
    pairs = []
    for i in range(len(sentence)):
        word = sentence[i]
        if word is None:
            continue
        reduced_window = random.randint(window)
        j = i - window + reduced_window

        if j < 0:
            j = 0
        k = i + window + 1 - reduced_window
        if k > len(sentence):
            k = len(sentence)
        for j in range(j, k):
            if j == i or sentence[j] is None:
                continue
            pairs.append((sentence[i], sentence[j]))

    #logging.info("{} samples generated from len {} sentence".format(len(pairs), len(sentence)))

    return pairs
