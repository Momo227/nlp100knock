from transformers import MarianMTModel
from transformers.models.marian.tokenization_marian import MarianTokenizer
from sacrebleu import corpus_bleu


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

    datas = [train_X, train_Y, valid_X, valid_Y, test_X, test_Y]

    for data in datas:
        for sentence in data:
            print(sentence.split())


if __name__ == '__main__':
    main()