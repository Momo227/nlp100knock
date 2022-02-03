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
    with open('../../data/ai.ja/ans46.txt', 'w') as f:
        for sentence in sentences:
            for chunk in sentence.chunks:
                for morph in chunk.morphs:
                    # chunkの左から順番に動詞を探す
                    if morph.pos == '動詞':
                        cases = []
                        sahen = []
                        # 動詞の係り元chunkから助詞を探す
                        # 係り元文節インデックス番号のリストから
                        for src in chunk.srcs:
                            # 文字
                            case = [morph.surface for morph in sentence.chunks[src].morphs if morph.pos == '助詞']
                            # 助詞を含むchunkの場合は助詞と項を取得
                            if len(case) > 0:
                                cases = cases + case
                                sahen.append(''.join(
                                    morph.surface for morph in sentence.chunks[src].morphs if morph.pos != '記号'))
                        # 助詞あり：重複除去後辞書順にソートし、項と合わせて出力
                        if len(cases) > 0:
                            cases = sorted(list(set(cases)))
                            line = '{}\t{}\t{}'.format(morph.base, ' '.join(cases), ' '.join(sahen))
                            print(line, file=f)
                        break


if __name__ == '__main__':
    main()
