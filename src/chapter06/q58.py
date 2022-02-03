import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from collections import Mapping, defaultdict
import matplotlib.pyplot as plt


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.feature.txt", sep="\t")
    train_test = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.feature.txt", sep="\t")
    test_test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    train_test = train_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})
    test_test = test_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})

    clf = LogisticRegression(random_state=2, max_iter=10000)
    clf.fit(train, train_test)

    for c in clf.coef_:
        # 全ての単語と特徴量のペアを作成
        d = dict(zip(train, c))
    # valueの値でソート
    top = sorted(d.items(), key=lambda x: abs(x[1]), reverse=True)[:10]
    bottom = sorted(d.items(), key=lambda x: abs(x[1]), reverse=False)[:10]

    print(top)
    print(bottom)


if __name__ == '__main__':
    main()
