import torch
import torch.nn as nn
import pytorch_lightning as pl
import torch.nn.functional as F
from torch.optim import SGD
from sklearn.linear_model import LogisticRegression
from torch.utils.data import DataLoader
from collections import defaultdict
import pandas as pd

class RNN(pl.LightningModule):

    # 埋め込み層, 隠れ層, 全結合層の定義
    def __init__(self, n_input, n_embed, n_hidden, n_layers, n_output, dropout, bidirectional):
        super(RNN, self).__init__()
        self.embed = nn.Embedding(num_embeddings=n_input, embedding_dim=n_embed, padding_idx=1)
        self.lstm = nn.LSTM(input_size=n_embed, hidden_size=n_hidden, num_layers=n_layers, dropout=dropout,
                            bidirectional=bidirectional)
        self.fc = nn.Linear(in_features=n_hidden * (2 if bidirectional == True else 1), out_features=n_output)

    # 順伝播
    def forward(self, x):
        o, (h, c) = self.lstm(self.embed(x))
        return self.fc(o[-1])

    # 訓練用データのバッチを受け取って損失を計算
    def training_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        loss = self.lossfun(y, t)
        self.log("train_loss", loss)
        return loss

    # 検証用データのバッチを受け取って損失を計算
    def validation_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        loss = self.lossfun(y, t)
        self.log("val_loss", loss)

    # 評価用データのバッチを受け取って分類の正解率を計算
    def test_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        y = torch.argmax(y, dim=1)
        accuracy = torch.sum(t == y).item() / (len(y) * 1.0)
        self.log("test_acc", accuracy)

    # 損失関数を設定
    def lossfun(self, y, t):
        return F.cross_entropy(y, t)

    # 最適化手法を設定
    def configure_optimizers(self):
        return torch.optim.Adam(self.parameters(), lr=0.01)
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
