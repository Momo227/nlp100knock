from gensim.models import KeyedVectors


def main():
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)

    print(model.similarity('United_States', 'U.S.'))


if __name__ == '__main__':
    main()



