import torch
import numpy as np


def main():
    # np -> torch
    X_train = np.loadtxt("../../data/NewsAggregatorDataset/train_vec.txt", delimiter=' ')
    X_train = torch.tensor(X_train, dtype=torch.float32)

    # ランダムな値で初期化
    W = torch.randn(300, 4)
    softmax = torch.nn.Softmax(dim=1)

    # matmul:行列の積

    # y1
    print(softmax(torch.matmul(X_train[:1], W)))

    # Y
    print(softmax(torch.matmul(X_train[:4], W)))


if __name__ == '__main__':
    main()
