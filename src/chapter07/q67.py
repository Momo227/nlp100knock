from gensim.models import KeyedVectors

def main():
    model = KeyedVectors.load_word2vec_format('../../data/GoogleNews-vectors-negative300.bin.gz', binary=True)


    with open("../../data/questions-words.txt") as input_file, open("../../data/questions-words.tsv", "w") as out_file:
        header = ["単語1" + "\t" + "単語2" + "\t" + "単語3" + "\t" + "類似語" + "\t" + "類似度"]
        out_file.write(header[0] + "\n")
        for row in input_file:
            if ": " in row:
                continue
            else:
                row = row.strip().split(" ")
                word, cos = model.most_similar(positive=[row[1], row[2]], negative=[row[0]], topn=1)[0]
                out_file.write(str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + "\t" + str(word) + "\t" + str(cos) + "\n")

if __name__ == '__main__':
    main()
