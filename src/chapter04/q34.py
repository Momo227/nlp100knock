def load_data(path):
    text = []
    datas = []
    with open(path) as input_file:
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
    for row in data:
        for i in range(1, len(row) - 1):
            if row[i - 1]['pos'] == '名詞' and row[i]['surface'] == 'の' and row[i + 1]['pos'] == '名詞':
                ans.add(row[i - 1]['surface'] + row[i]['surface'] + row[i + 1]['surface'])


    print(ans)


if __name__ == '__main__':
    main()
