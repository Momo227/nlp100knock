import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import collections
from collections import defaultdict


def main():
    train = pd.read_csv("../../data/NewsAggregatorDataset/train.txt", sep='\t')

    # ユニークな → 重複しない

    train = train["title"]

    data = defaultdict(int)
    for row in train:
        words = row.split()
        for word in words:
            data[word] += 1

    data = sorted(data.items(), key=lambda x: x[1], reverse=True)

    i = 1
    ans = defaultdict(int)
    for k, v in data:
        if v == 1:
            ans[k] = 0
        else:
            ans[k] = i
            i += 1

    print(ans)


if __name__ == '__main__':
    main()
