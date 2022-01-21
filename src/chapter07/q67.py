from gensim.models import KeyedVectors
from sklearn.cluster import KMeans
import numpy as np

def main():
    data = []
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)
    with open('../../data/country_name.txt') as f:
        countries = f.readlines()

    for country in countries:
        country = country.replace("\n", "")
        data.append(country)

    d2v = []
    for i in range(len(data)):
        d2v.append(model[data[i]])


    # k-meansクラスタリング
    kmeans = KMeans(5)
    kmeans.fit(d2v)

    for i in range(5):
        cluster = np.where(kmeans.labels_ == i)[0]
        print('cluster', i)
        print(', '.join([countries[k] for k in cluster]))

if __name__ == '__main__':
    main()
