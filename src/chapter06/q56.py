import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score
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

    # 適合率
    precision = precision_score(test_test, clf.predict(test), average=None)
    print(["e", "b", "m", "t"])
    print(precision)
    precision_micro_average = precision_score(test_test, clf.predict(test), average='micro')
    precision_macro_average = precision_score(test_test, clf.predict(test), average='macro')
    print('precisionミクロ平均：' + str(precision_micro_average))
    print('precisionマクロ平均：' + str(precision_macro_average))

    # 再現率
    recall = recall_score(test_test, clf.predict(test), average=None)
    print(["e", "b", "m", "t"])
    print(recall)
    recall_micro_average = recall_score(test_test, clf.predict(test), average='micro')
    recall_macro_average = recall_score(test_test, clf.predict(test), average='macro')
    print('recallミクロ平均：' + str(recall_micro_average))
    print('recallマクロ平均：' + str(recall_macro_average))

    # F1スコア
    f1 = f1_score(test_test, clf.predict(test), average=None)
    print(["e", "b", "m", "t"])
    print(f1)
    f1_micro_average = f1_score(test_test, clf.predict(test), average='micro')
    f1_macro_average = f1_score(test_test, clf.predict(test), average='macro')
    print('f1ミクロ平均：' + str(f1_micro_average))
    print('f1マクロ平均：' + str(f1_macro_average))


if __name__ == '__main__':
    main()
