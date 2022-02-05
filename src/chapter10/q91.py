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


src_field = Field(sequential=True, use_vocab=True, init_token="<s>", eos_token="</s>")
tgt_field = Field(sequential=True, use_vocab=True, init_token="<s>", eos_token="</s>")
fields = [("src", src_field), ("tgt", tgt_field)]


def load_corpus(fname, src, tgt):
    # ソース言語のデータを単語リストのリストに変換
    fin = open(fname + ".%s" % src, "r")
    src_data = [line.strip().split() for line in fin]
    fin.close()
    # ターゲット言語のデータを単語リストのリストに変換
    fin = open(fname + ".%s" % tgt, "r")
    tgt_data = [line.strip().split() for line in fin]
    fin.close()
    # データセットオブジェクトに変換
    examples = [Example.fromlist([src_words, tgt_words], fields) for src_words, tgt_words in zip(src_data, tgt_data)]
    return Dataset(examples, fields)


# ====================
# モデルの定義
# ====================

class Encoder(nn.Module):

    def __init__(self, n_words_src, n_embed, n_hidden, n_layers):
        super(Encoder, self).__init__()
        self.embed = nn.Embedding(num_embeddings=n_words_src, embedding_dim=n_embed)
        self.lstm = nn.LSTM(input_size=n_embed, hidden_size=n_hidden, num_layers=n_layers)

    def forward(self, src_text):
        x = self.embed(src_text)
        o, (h, c) = self.lstm(x)
        return h, c


class Decoder(nn.Module):

    def __init__(self, n_words_tgt, n_embed, n_hidden, n_layers):
        super(Decoder, self).__init__()
        self.tgt_vocab_size = n_words_tgt
        self.embed = nn.Embedding(num_embeddings=n_words_tgt, embedding_dim=n_embed)
        self.lstm = nn.LSTM(input_size=n_embed, hidden_size=n_hidden, num_layers=n_layers)
        self.lstm = nn.LSTM(input_size=n_embed, hidden_size=n_hidden, num_layers=n_layers)
        self.lstm = nn.LSTM(input_size=n_embed, hidden_size=n_hidden, num_layers=n_layers)
        self.fc = nn.Linear(in_features=n_hidden, out_features=n_words_tgt)

    def forward(self, x, h, c):
        x = self.embed(x.unsqueeze(0))
        o, (h, c) = self.lstm(x, (h, c))
        o = self.fc(o.squeeze(0))
        return o, h, c


class RNN_NMT(nn.Module):

    def __init__(self, encoder, decoder, device):
        super(RNN_NMT, self).__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.device = device

    def forward(self, src_text, tgt_text, training):
        # エンコード
        h, c = self.encoder(src_text)
        # 出力用テンソルの準備
        tgt_len, batch_size = tgt_text.shape
        outputs = torch.zeros(tgt_len, batch_size, self.decoder.tgt_vocab_size).to(self.device)
        # 文頭の特殊トークン<s>の抽出
        x = tgt_text[0, :]
        # デコード
        for t in range(1, tgt_len):
            # 次の単語の確率分布を出力
            o, h, c = self.decoder(x, h, c)
            outputs[t] = o
            # 次の時刻の入力として、訓練時（training==True）には正解文から単語を取り出して使う
            if training and random.random() < 0.5:
                x = tgt_text[t]
            # 次の時刻の入力として、評価時には前の時刻で出力した単語を使う
            else:
                x = o.argmax(1)
        return outputs


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
    # test_tokenize_X = tokenize_english(test_X)

    # 日本語の形態素解析
    # tagger = MeCab.Tagger()
    # train_tokenize_Y = tokenize_japanese(train_Y, tagger)
    # valid_tokenize_Y = tokenize_japanese(valid_Y, tagger)
    # test_tokenize_Y = tokenize_japanese(test_Y, tagger)

    # 語彙を登録（訓練データに含まれる単語にIDを割り振る）
    src_field.build_vocab(train_X, min_freq=3)
    tgt_field.build_vocab(train_Y, min_freq=3)

    # データセットオブジェクトからデータローダーを作成
    dataloader_train = BucketIterator(train_tokenize_X, batch_size=batch_size, shuffle=True, device=device)
    dataloader_val = BucketIterator(valid_tokenize_X, batch_size=batch_size, shuffle=False, device=device)

    # ハイパーパラメータ
    n_words_src = len(src_field.vocab)
    n_words_tgt = len(tgt_field.vocab)
    n_embed = 256
    n_hidden = 512
    n_layers = 2
    learning_rate = 0.01
    max_epoch = 15

    # モデルの設定
    encoder = Encoder(n_words_src, n_embed, n_hidden, n_layers)
    decoder = Decoder(n_words_tgt, n_embed, n_hidden, n_layers)
    model = RNN_NMT(encoder, decoder, device).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    criterion = nn.CrossEntropyLoss(ignore_index=tgt_field.vocab.stoi[tgt_field.pad_token])

    print(model)

    # ====================
    # 訓練
    # ====================

    def train(model, dataloader, optimizer, criterion):
        model.train()
        epoch_loss = 0
        for batch in dataloader:
            # 推論の準備
            src = batch.src
            tgt = batch.tgt
            optimizer.zero_grad()
            # 推論
            pred = model(src, tgt, training=True)
            # 損失計算の準備
            pred = pred[1:].view(-1, pred.shape[-1])
            tgt = tgt[1:].view(-1)
            # 損失計算
            loss = criterion(pred, tgt)
            epoch_loss += loss.item()
            # 逆伝播
            loss.backward()
            optimizer.step()
        return epoch_loss / len(dataloader)

    def valid(model, dataloader, criterion):
        model.eval()
        epoch_loss = 0
        for batch in dataloader:
            # 推論の準備
            src = batch.src
            tgt = batch.tgt
            # 推論
            pred = model(src, tgt, training=False)
            # 損失計算の準備
            pred = pred[1:].view(-1, pred.shape[-1])
            tgt = tgt[1:].view(-1)
            # 損失計算
            loss = criterion(pred, tgt)
            epoch_loss += loss.item()
        return epoch_loss / len(dataloader)

    best_valid_loss = float("inf")
    for epoch in range(max_epoch):
        train_loss = train(model, dataloader_train, optimizer, criterion)
        val_loss = valid(model, dataloader_val, criterion)
        # モデルの保存
        if val_loss < best_valid_loss:
            best_valid_loss = val_loss
            torch.save(model.state_dict(), "rnn.model")
        # 損失の表示
        print("Epoch: %02d\tTrain Loss = %.3f\tValid Loss = %.3f" % (epoch + 1, train_loss, val_loss))


if __name__ == '__main__':
    main()
