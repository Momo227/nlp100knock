import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    data = pd.read_csv('../../data/NewsAggregatorDataset/newsCorpora.csv', header=None, names=['id', 'title', 'url', 'publisher', 'category', 'story', 'name', 'time'], sep='\t', quoting=3)

    mini_data = data.loc[data['publisher'].isin(['Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail']), ['title', 'category']]

    train, valid = train_test_split(mini_data, test_size=0.2, shuffle=True, random_state=2, stratify=mini_data['category'])
    valid, test = train_test_split(valid, test_size=0.5, shuffle=True, random_state=2, stratify=valid['category'])

    # データの保存
    train.to_csv('../../data/NewsAggregatorDataset/train.txt', sep='\t', index=False)
    valid.to_csv('../../data/NewsAggregatorDataset/valid.txt', sep='\t', index=False)
    test.to_csv('../../data/NewsAggregatorDataset/test.txt', sep='\t', index=False)

    print("train data")
    print(train['category'].value_counts())
    print("dev data")
    print(valid['category'].value_counts())
    print("test data")
    print(test['category'].value_counts())

if __name__ == '__main__':
    main()
