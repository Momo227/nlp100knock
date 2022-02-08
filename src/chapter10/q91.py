import MeCab
import nltk
from nltk.tokenize import word_tokenize
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchtext.legacy.data import Example, Field, Dataset, BucketIterator

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
nltk.download('punkt')

# 入出力の言語とバッチサイズを指定
src = "en"
tgt = "ja"
batch_size = 64


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


# データの読み込み
src_field = Field(sequential=True, use_vocab=True, init_token="<sos>", eos_token="<eos>", batch_first=True)
tgt_field = Field(sequential=True, use_vocab=True, init_token="<sos>", eos_token="<eos>", batch_first=True)
fields = [("src", src_field), ("tgt", tgt_field)]

def load_corpus(fname, lang_src, lang_tgt):
    # ソース言語
    fin = open(fname + ".%s" % lang_src, "r")
    src_data = [line.strip().split() for line in fin]
    fin.close()
    # ターゲット言語
    fin = open(fname + ".%s" % lang_tgt, "r")
    tgt_data = [line.strip().split() for line in fin]
    fin.close()
    # データセットオブジェクトに変換
    examples = [Example.fromlist([src_words, tgt_words], fields) for src_words, tgt_words in zip(src_data, tgt_data)]
    return Dataset(examples, fields)


def main():
    print("load_data")
    # with open(
    #         "../../data/kyoto-train.en") as train_x, open(
    #     "../../data/kyoto-train.ja") as train_y, open(
    #     "../../data/kyoto-dev.en") as valid_x, open(
    #     "../../data/kyoto-dev.ja") as valid_y, open(
    #     "../../data/kyoto-test.en") as test_x, open(
    #     "../../data/kyoto-test.ja") as test_y:
    #     train_X = train_x.read()
    #     train_Y = train_y.read()
    #     valid_X = valid_x.read()
    #     valid_Y = valid_y.read()
    #     test_X = test_x.read()
    #     test_Y = test_y.read()

    # print("make list of test")
    # train_X = [sentence for sentence in train_X.split("\n")][:-1]
    # train_Y = [sentence for sentence in train_Y.split("\n")][:-1]
    # valid_X = [sentence for sentence in valid_X.split("\n")][:-1]
    # valid_Y = [sentence for sentence in valid_Y.split("\n")][:-1]
    # test_X = [sentence for sentence in test_X.split("\n")][:-1]
    # test_Y = [sentence for sentence in test_Y.split("\n")][:-1]
    #
    # # 英語の形態素解析
    # train_tokenize_X = tokenize_english(train_X)
    # print(train_tokenize_X)
    # exit()
    # valid_tokenize_X = tokenize_english(valid_X)
    # test_tokenize_X = tokenize_english(test_X)
    #
    #
    # # 日本語の形態素解析
    # tagger = MeCab.Tagger()
    # train_tokenize_Y = tokenize_japanese(train_Y, tagger)
    # valid_tokenize_Y = tokenize_japanese(valid_Y, tagger)
    # test_tokenize_Y = tokenize_japanese(test_Y, tagger)

    dataset_train = load_corpus("../../data/kyoto-train", src, tgt)
    dataset_val = load_corpus("../../data/kyoto-dev", src, tgt)

    # print("give ID")
    # # 語彙を登録（訓練データに含まれる単語にIDを割り振る）
    # src_field.build_vocab(dataset_train, min_freq=3)
    # tgt_field.build_vocab(dataset_train, min_freq=3)
    #
    # print("make dataloader")
    # # データセットオブジェクトからデータローダーを作成
    # dataloader_train = BucketIterator(dataset=train_tokenize_X, batch_size=batch_size, shuffle=True, device=device)
    # dataloader_val = BucketIterator(valid_tokenize_X, batch_size=batch_size, shuffle=False, device=device)

    # 訓練用・検証用・評価用データの件数
    print("Number of training examples: %d" % len(dataset_train))
    print("Number of validation examples: %d" % len(dataset_val))

    # ソース言語とターゲット単語の語彙サイズ
    print("\nNumber of source words: %d" % len(src_field.vocab))
    print("Number of target words: %d" % len(tgt_field.vocab))



if __name__ == '__main__':
    main()
