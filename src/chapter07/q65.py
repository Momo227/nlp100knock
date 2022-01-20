import pandas as pd

def main():

    data = pd.read_csv("../../data/questions-words.tsv", sep='\t')
    word1 = data["単語4"]
    word2 = data["類似語"]

    cnt1 = 0
    for i in range(8870):
        if word1[i] == word2[i]:
            cnt1 += 1

    cnt2 = 0
    lng = len(data)
    for i in range(lng - 8870):
        if word1[i+8870] == word2[i+8870]:
            cnt2 += 1

    print(cnt1/8870)
    print(cnt2/(lng-8870))



if __name__ == '__main__':
    main()
