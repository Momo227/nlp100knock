import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import numpy as np


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.feature.txt", sep="\t")
    train_test = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    valid = pd.read_csv("../../data/NewsAggregatorDataset/valid.feature.txt", sep="\t")
    valid_test = pd.read_csv("../../data/NewsAggregatorDataset/valid.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.feature.txt", sep="\t")
    test_test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    train_test = train_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})
    valid_test = valid_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})
    test_test = test_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})

    # C ：正則化パラメータ

    C = [0.01, 0.1, 1]
    score = []
    for c in C:
        print(c)
        clf = LogisticRegression(random_state=2, max_iter=10000, C=c)
        clf.fit(train, train_test)

        print(accuracy_score(train_test, clf.predict(train)))
        print(accuracy_score(valid_test, clf.predict(valid)))
        print(accuracy_score(test_test, clf.predict(test)))

        score.append([c, accuracy_score(train_test, clf.predict(train)), accuracy_score(valid_test, clf.predict(valid)), accuracy_score(test_test, clf.predict(test))])

    result = np.array(score).T
    plt.plot(result[0], result[1], label='train')
    plt.plot(result[0], result[2], label='valid')
    plt.plot(result[0], result[3], label='test')
    plt.ylim(0, 1.1)
    plt.ylabel('Accuracy')
    plt.xscale('log')
    plt.xlabel('C')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
