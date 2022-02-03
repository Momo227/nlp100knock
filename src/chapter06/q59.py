import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.tree import DecisionTreeClassifier


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.feature.txt", sep="\t")
    train_test = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.feature.txt", sep="\t")
    test_test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    train_test = train_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})
    test_test = test_test['category'].map({'e': 0, 'b': 1, 'm': 2, 't': 3})

    # LogisticRegression
    C = [0.01, 0.1, 1]

    best_model = ""
    best_param = ""
    best_score = 0
    print("LogisticRegression")
    for c in C:
        print(c)
        clf = LogisticRegression(random_state=2, max_iter=10000, C=c)
        clf.fit(train, train_test)

        print(accuracy_score(test_test, clf.predict(test)))

        if best_score < accuracy_score(test_test, clf.predict(test)):
            best_model = "LogisticRegression"
            best_param = c
            best_score = accuracy_score(test_test, clf.predict(test))

    # LinearSVC
    C = [0.01, 0.1, 1]
    print("LinearSVC")
    for c in C:
        clf = LinearSVC(C=c)
        clf.fit(train, train_test)
        print(accuracy_score(test_test, clf.predict(test)))

        if best_score < accuracy_score(test_test, clf.predict(test)):
            best_model = "LinearSVC"
            best_param = c
            best_score = accuracy_score(test_test, clf.predict(test))

    # 決定木
    print("決定木")
    clf = DecisionTreeClassifier(max_depth=4)
    clf.fit(train, train_test)

    print(accuracy_score(test_test, clf.predict(test)))

    if best_score < accuracy_score(test_test, clf.predict(test)):
        best_model = "決定木"
        best_param = None
        best_score = accuracy_score(test_test, clf.predict(test))

    print("ベストモデル：" + best_model)
    print("ベストパラメータ：" + str(best_param))
    print("ベストスコア：" + str(best_score))


if __name__ == '__main__':
    main()
