## Word2vec with custom sampling

This is a Python implementation of the word2vec algorithm.

The major part of this code was written by Radim Rehurek and was extracted from the `gensim` topic modelling library.
I added code that abstracts the sampling step of the algorithm, making it more convenient to try out new sampling strategies.

When initializing the Word2Vec class, you now need to specify a sampling function. Given a sentence, it should return
 a list of pairs of vocabulary items (`Vocab`). For instance:

`model = Word2Vec(Text8Corpus(infile), size=200, min_count=5, workers=1, sampler=sampling_fn)`

Although version is not quite as fast as the original (it gives ~50% throughput) it still beats a pure Python implementation
by a factor of at least 50.

## Demo

run `python word2vec.py data/text8data/questions-words.txt`


## Example: The original sampling strategy implemented as a function

``
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

    return pairs
``