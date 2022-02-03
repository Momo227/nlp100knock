from itertools import combinations
import re


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
    sentence = sentences[2]
    nouns = []
    # インデックスも作成
    for i, chunk in enumerate(sentence.chunks):
        # 名詞を含む文節のインデックスを抽出
        if '名詞' in [morph.pos for morph in chunk.morphs]:
            nouns.append(i)
    # 名詞を含む文節のペアごとにパスを作成
    for i, j in combinations(nouns, 2):
        path_i = []
        path_j = []
        # パス作成中　同じ数＝末端になったら終了
        while i != j:
            if i < j:
                path_i.append(i)
                i = sentence.chunks[i].dst
            else:
                path_j.append(j)
                j = sentence.chunks[j].dst

        # 文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示について
        # i の係り受け先に j がある
        if len(path_j) == 0:
            # 名詞以外だったら pass、名詞はX or Y に置換
            # X -> 先頭
            # Y -> かかり先
            chunk_X = ''.join(
                [morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
            chunk_Y = ''.join([morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[i].morphs])

            # X や Y が複数あったら1つに
            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)

            # X (先頭) + 文節（中間）　+ Y (文末)
            path_XtoY = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in
                                     path_i[1:]] + [chunk_Y]
            print(' -> '.join(path_XtoY))
        # 上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合: 文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を” | “で連結して表示
        else:
            chunk_X = ''.join(
                [morph.surface if morph.pos != '名詞' else 'X' for morph in sentence.chunks[path_i[0]].morphs])
            chunk_Y = ''.join(
                [morph.surface if morph.pos != '名詞' else 'Y' for morph in sentence.chunks[path_j[0]].morphs])
            # 共通文節
            chunk_k = ''.join([morph.surface for morph in sentence.chunks[i].morphs])

            chunk_X = re.sub('X+', 'X', chunk_X)
            chunk_Y = re.sub('Y+', 'Y', chunk_Y)

            # かかり関係のリスト
            path_X = [chunk_X] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_i[1:]]
            path_Y = [chunk_Y] + [''.join(morph.surface for morph in sentence.chunks[n].morphs) for n in path_j[1:]]

            # リストを -> で接続　→　共通するものを | で接続
            print(' | '.join([' -> '.join(path_X), ' -> '.join(path_Y), chunk_k]))


if __name__ == '__main__':
    main()
