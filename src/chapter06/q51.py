import pandas as pd
import re
import string
from sklearn.feature_extraction.text import TfidfVectorizer


def preprocessing(text):
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    text = text.translate(table)  # 記号をスペースに置換
    text = text.lower()  # 小文字化
    text = re.sub('[0-9]+', '0', text)  # 数字列を0に置換

    return text


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    valid = pd.read_csv("../../data/NewsAggregatorDataset/valid.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    df = pd.concat([train, valid, test], axis=0)
    df.reset_index(drop=True, inplace=True)  # indexを振りなおす

    # 前処理の実施
    df['title'] = df['title'].map(lambda x: preprocessing(x))

    train_valid = df[:len(train) + len(valid)]
    test = df[len(train) + len(valid):]

    # TfidfVectorizer
    vec_BoW = TfidfVectorizer(min_df=10, ngram_range=(1, 2))

    # ベクトル化
    X_train_valid = vec_BoW.fit_transform(train_valid['title'])
    X_test = vec_BoW.transform(test['title'])

    # ベクトルをデータフレームに変換
    X_train_valid = pd.DataFrame(X_train_valid.toarray(), columns=vec_BoW.get_feature_names())
    X_test = pd.DataFrame(X_test.toarray(), columns=vec_BoW.get_feature_names())

    # データの分割
    X_train = X_train_valid[:len(train)]
    X_valid = X_train_valid[len(train):]

    # データの保存
    X_train.to_csv('../../data/NewsAggregatorDataset/train.feature.txt', sep='\t', index=False)
    X_valid.to_csv('../../data/NewsAggregatorDataset/valid.feature.txt', sep='\t', index=False)
    X_test.to_csv('../../data/NewsAggregatorDataset/test.feature.txt', sep='\t', index=False)


if __name__ == '__main__':
    main()
