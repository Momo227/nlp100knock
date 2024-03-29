class Morph:
    def __init__(self, morph):
        (surface, attr) = morph.split("\t")
        attr = attr.split(",")
        self.surface = surface
        self.base = attr[6]
        self.pos = attr[0]
        self.pos1 = attr[1]


class Chunk():
    def __init__(self, morphs, dst):
        self.morphs = morphs
        # 自分から出る矢印は1本
        self.dst = dst
        self.srcs = []


# かかり先から逆向きに設定し、かかり関係をつける
class Sentence():
    def __init__(self, chunks):
        self.chunks = chunks
        for i, chunk in enumerate(self.chunks):
            # 係り受け先がある場合 : かかり元が自分であると示す
            if chunk.dst not in [None, -1]:
                self.chunks[chunk.dst].srcs.append(i)


def main():
    sentences = []
    chunks = []
    morphs = []
    with open("../../data/ai.ja/ai.ja.txt.paresd") as input_file:
        for line in input_file:
            # 係り受け関係を示すもの
            if line[0] == "*":
                if len(morphs) > 0:
                    chunks.append(Chunk(morphs, dst))
                    morphs = []
                # 係り先の単語のID
                dst = int(line.split(" ")[2].rstrip("D"))
            # 文末以外：形態素リスト追加
            elif line != "EOS\n":
                morphs.append(Morph(line))
            # 文末
            else:
                chunks.append(Chunk(morphs, dst))
                sentences.append(Sentence(chunks))
                morphs = []
                chunks = []
                dst = None

    # 追加
    with open('../../data/ai.ja/ans45.txt', 'w') as f:
        for sentence in sentences:
            for chunk in sentence.chunks:
                for morph in chunk.morphs:
                    if morph.pos == '動詞':
                        cases = []
                        # 見つけた動詞の係り元chunkから助詞を探す
                        for src in chunk.srcs:
                            cases = cases + [morph.surface for morph in sentence.chunks[src].morphs if
                                             morph.pos == '助詞']

                        # 助詞が見つかった場合は重複除去後辞書順にソートして出力
                        if len(cases) > 0:
                            cases = sorted(list(set(cases)))
                            line = '{}\t{}'.format(morph.base, ' '.join(cases))
                            print(line, file=f)
                        break


if __name__ == '__main__':
    main()
