from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


def main():
    data = []
    # model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)
    with open('../../data/questions-words.txt') as f:
        for line in f:
            line = line.split()
            if line[0] in 'capital-common-countries' or line[0] in'capital-world':
                print(line)
                data.append(line[2])
            elif line[0] in 'currency' or line[0] in 'gram6-nationality-adjective':
                print(line)
                data.append(line[1])
        data = list(data)

        print(data)

    d2v = [model[word] for word in data]

    print(d2v)
    # k-meansクラスタリング
    kmeans = KMeans(5)
    kmeans.fit(d2v)

    print(kmeans.labels_)

if __name__ == '__main__':
    main()
