import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.feature.txt", sep="\t")
    train_test = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.feature.txt", sep="\t")
    test_test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    train_test = train_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})
    test_test = test_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})

    clf = LogisticRegression(random_state=2, max_iter=10000)
    clf.fit(train, train_test)

    print(confusion_matrix(train_test, clf.predict(train)))
    print(confusion_matrix(test_test, clf.predict(test)))


if __name__ == '__main__':
    main()
