from scipy.stats import spearmanr
from gensim.models import KeyedVectors

def main():
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)
    sim = []
    with open("../../data/wordsim353/combined.csv") as f:
        next(f)
        data = f.read()

        data = data.split("\n")
        human = []
        for i in range(len(data)-1):
            row = [mini.strip() for mini in data[i].split(",")]
            print(row)
            human.append(row[2])
            sim.append(model.similarity(row[0], row[1]))


    correlation, pvalue = spearmanr(sim, human)

    print(correlation)

if __name__ == '__main__':
    main()
