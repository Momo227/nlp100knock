import torch
import numpy as np
import torch.nn as nn

class Perceptron(nn.Module):
    def __init__(self, v_size, c_size):
        super().__init__()
        self.fc = nn.Linear(v_size, c_size, bias = False)
        nn.init.xavier_normal_(self.fc.weight)

    def forward(self, x):
        x = self.fc(x)
        return x

def main():
    # np -> torch
    X_train = np.loadtxt("../../data/NewsAggregatorDataset/train_vec.txt", delimiter=' ')
    X_train = torch.tensor(X_train, dtype=torch.float32)
    Y_train = np.loadtxt("../../data/NewsAggregatorDataset/train_ans.csv", delimiter=' ')
    Y_train = torch.tensor(Y_train, dtype=torch.float32)

    print(X_train)
    print(Y_train)
    criterion = nn.CrossEntropyLoss()

    y = (X_train[:1])
    t = Y_train[:1]
    loss = criterion(y, t)

    model = Perceptron(300, 4)

    model.zero_grad()
    loss.backward()
    print('損失 :', loss.item())
    print('勾配')
    print(model.fc.weight.grad)

    # # ランダムな値で初期化
    # W = torch.randn(300, 4)
    # softmax = torch.nn.Softmax(dim=1)
    #
    #
    # loss = torch.nn.CrossEntropyLoss()
    # print(loss(torch.matmul(X_train[:1], W), Y_train[:1]))
    # print(loss(torch.matmul(X_train[:4], W), Y_train[:4]))
    # # y1
    # ans = []  # 以下、確認
    # for s, i in zip(softmax(torch.matmul(X_train[:4], W)), Y_train[:4]):
    #     ans.append(-np.log(s[i]))
    # print(np.mean(ans))


if __name__ == '__main__':
    main()
