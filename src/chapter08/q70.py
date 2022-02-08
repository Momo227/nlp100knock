import pandas as pd
import numpy as np
from gensim.models import KeyedVectors


def make_vec(file_name, sentences, model):
    with open(file_name, 'w') as f:
        vec_X = []
        for sentence in sentences:
            sentence = sentence.split()
            for word in sentence:
                try:
                    vec_X.append(model[word])
                except:
                    continue
            if (len(vec_X) == 0):
                vector = np.zeros(300)
            else:
                vec_X = np.array(vec_X)
                vector = vec_X.mean(axis=0)
            vector = vector.astype(np.str).tolist()
            output = ' '.join(vector) + '\n'
            f.write(output)


def main():
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)

    train = pd.read_csv("../../data/train.txt", sep="\t")
    train_X = train["title"]
    train_Y = train["category"]
    valid = pd.read_csv("../../data/valid.txt", sep="\t")
    valid_X = valid["title"]
    valid_Y = valid["category"]
    test = pd.read_csv("../../data/test.txt", sep="\t")
    test_X = test["title"]
    test_Y = test["category"]

    train_Y = train_Y.map({'b': 0, 't': 1, 'e': 2, 'm': 3})
    valid_Y = valid_Y.map({'b': 0, 't': 1, 'e': 2, 'm': 3})
    test_Y = test_Y.map({'b': 0, 't': 1, 'e': 2, 'm': 3})

    make_vec('../../data/train_vec.txt', train_X, model)
    make_vec('../../data/dev_vec.txt', valid_X, model)
    make_vec('../../data/test_vec.txt', test_X, model)

    train_Y.to_csv('../../data/train_ans.csv', header=False, index=False)
    valid_Y.to_csv('../../data/valid_ans.csv', header=False, index=False)
    test_Y.to_csv('../../data/test_ans.csv', header=False, index=False)


if __name__ == '__main__':
    main()
