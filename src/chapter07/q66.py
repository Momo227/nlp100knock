from gensim.models import KeyedVectors
from sklearn.cluster import KMeans


def main():
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)

    # k-meansクラスタリング
    kmeans = KMeans(n_clusters=5)
    kmeans.fit(countries_vec)

if __name__ == '__main__':
    main()
