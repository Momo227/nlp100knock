class Morph:
    def __init__(self, morph):
        (surface, attr) = morph.split("\t")
        attr = attr.split(",")
        self.surface = surface
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]


def main():
    sentences = []
    sentence = []
    with open('../../data/ai.ja/ai.ja.txt.paresd') as f:
        for line in f:
           # 係り受け関係を示すものを飛ばす
            if line[0] == "*":
                continue
            # 本文
            elif line != "EOS\n":
                sentence.append(Morph(line))
            # 文末
            else:
                sentences.append(sentence)
                sentence = []


    for morph in sentences[2]:
        # vars：現在のローカルシンボルテーブルを表す辞書を更新して示す
        print(vars(morph))


if __name__ == '__main__':
    main()
