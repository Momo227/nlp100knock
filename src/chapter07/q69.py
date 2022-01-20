from gensim.models import KeyedVectors
from matplotlib import pyplot as plt
import bhtsne
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

    embedded = bhtsne.tsne(np.array(d2v).astype(np.float64), dimensions=2, rand_seed=123)
    plt.figure(figsize=(10, 10))
    plt.scatter(np.array(embedded).T[0], np.array(embedded).T[1])
    for (x, y), name in zip(embedded, countries):
        plt.annotate(name, (x, y))
    plt.show()


if __name__ == '__main__':
    main()
