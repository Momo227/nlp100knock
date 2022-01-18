def load_data():
    text = []
    datas = []
    with open("data/neko.txt.mecab") as input_file:
        for row in input_file:

            # 文末以外：形態素解析情報をリストに追加
            if row != 'EOS\n':
                fields = row.split('\t')

                # 文頭以外の空白と改行文字は無視
                if len(fields) != 2 or fields[0] == '':
                    continue
                else:
                    mini_data = fields[1].split(',')
                    data = {'surface': fields[0], 'base': mini_data[6], 'pos': mini_data[0], 'pos1': mini_data[1]}
                    datas.append(data)
            # 文末：形態素リストを文リストに追加
            else:
                text.append(datas)
                datas = []

    return text


def main():
    data = load_data("data/neko.txt.mecab")

    ans = set()
    for lis in data:
        for part in lis:
            if part['pos'] == '動詞':
                ans.add(part['base'])

    print(ans)


if __name__ == '__main__':
    main()
