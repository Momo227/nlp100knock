from gensim.models import KeyedVectors
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage

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

    plt.figure(figsize=(15, 5))
    Z = linkage(d2v, method='ward')
    dendrogram(Z, labels=countries)
    plt.show()


if __name__ == '__main__':
    main()
