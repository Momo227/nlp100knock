import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

def normalize_number(text):
    replace_text = re.sub(r'\d', '0', text)
    return replace_text

def preprocessing(text):
  # 文字数を変えずに数字を０に置き換える
  text = normalize_number(text)
  return text


def main():

    train = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep="\t")
    valid = pd.read_csv("../../data/NewsAggregatorDataset/valid.txt", sep="\t")
    test = pd.read_csv("../../data/NewsAggregatorDataset/test.txt", sep="\t")

    # データの前処理
    train["title"] = train["title"].map(lambda x: preprocessing(x))
    valid["title"] = valid["title"].map(lambda x: preprocessing(x))
    test["title"] = test["title"].map(lambda x: preprocessing(x))

    # CountVectorizerによるBoW形式の特徴抽出
    cv = CountVectorizer()
    train_title = cv.fit_transform(train["title"]).toarray()
    valid_title = cv.fit_transform(valid["title"]).toarray()
    test_title = cv.fit_transform(test["title"]).toarray()

    # print(test_title)

    # データフレームに変換
    train = pd.DataFrame(list(zip(train_title, train["category"])), columns=['title', 'category'])
    valid = pd.DataFrame(list(zip(valid_title, valid["category"])), columns=['title', 'category'])
    test = pd.DataFrame(list(zip(test_title, test["category"])), columns=['title', 'category'])

    train.to_csv('../../data/NewsAggregatorDataset/train.feature.txt', sep='\t', index=False)
    valid.to_csv('../../data/NewsAggregatorDataset/valid.feature.txt', sep='\t', index=False)
    test.to_csv('../../data/NewsAggregatorDataset/test.feature.txt', sep='\t', index=False)


if __name__ == '__main__':
    main()
