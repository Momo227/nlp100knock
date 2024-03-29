import MeCab
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')


def tokenize_english(sentences):
    result = []
    for i in range(len(sentences)):
        result.append(word_tokenize(sentences[i]))

    return result


def tokenize_japanese(sentences, tagger):
    result = []
    for i in range(len(sentences)):
        result.append(tagger.parse(sentences[i]))

    return result


def main():
    print("load_data")
    with open(
            "../../data/kyoto-train.en") as train_x, open(
        "../../data/kyoto-train.ja") as train_y, open(
        "../../data/kyoto-dev.en") as valid_x, open(
        "../../data/kyoto-dev.ja") as valid_y, open(
        "../../data/kyoto-test.en") as test_x, open(
        "../../data/kyoto-test.ja") as test_y:
        train_X = train_x.read()
        train_Y = train_y.read()
        valid_X = valid_x.read()
        valid_Y = valid_y.read()
        test_X = test_x.read()
        test_Y = test_y.read()

    print("make list of test")
    train_X = [sentence for sentence in train_X.split("\n")][:-1]
    train_Y = [sentence for sentence in train_Y.split("\n")][:-1]
    valid_X = [sentence for sentence in valid_X.split("\n")][:-1]
    valid_Y = [sentence for sentence in valid_Y.split("\n")][:-1]
    test_X = [sentence for sentence in test_X.split("\n")][:-1]
    test_Y = [sentence for sentence in test_Y.split("\n")][:-1]

    # 英語の形態素解析
    train_tokenize_X = tokenize_english(train_X)
    valid_tokenize_X = tokenize_english(valid_X)
    test_tokenize_X = tokenize_english(test_X)

    # 日本語の形態素解析
    tagger = MeCab.Tagger()
    train_tokenize_Y = tokenize_japanese(train_Y, tagger)
    valid_tokenize_Y = tokenize_japanese(valid_Y, tagger)
    test_tokenize_Y = tokenize_japanese(test_Y, tagger)


    # 確認
    print(train_tokenize_X[10])
    print(test_tokenize_Y[10])


if __name__ == '__main__':
    main()
