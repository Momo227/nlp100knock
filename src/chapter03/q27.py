import re
from collections import defaultdict
import json

def load_data(file_path):
    with open(file_path, mode='r') as f:
        for line in f:
            line = json.loads(line)
            if line['title'] == 'イギリス':
                text = line['text']
                break
    return text

def remove_markup(x):
    # 強調マークアップの除去
    pattern = r'\'{2,5}'
    text = re.sub(pattern, '', x)

    # 内部リンクマークアップの除去
    pattern = r'\[\[(?:[^|]*?\|)??([^|]*?)\]\]'
    text = re.sub(pattern, r'\1', text)

    return text

def main():
    data = load_data('data/jawiki-country.json')

    # 基本情報の抽出
    # コンパイルタグ→+で加算
    # re.MULTILINE : ^や$で複数行文字列に対するマッチングを行う
    # re.IGNORECASE : 大文字小文字を区別しない
    # re.VERBOSE : 正規表現内のコメントと空白無視
    # re.DOTALL : .を改行を含む任意の文字に設定
    pattern = r'^\{\{基礎情報.*?$(.*?)^\}\}'
    template = re.findall(pattern, data, re.MULTILINE + re.DOTALL)

    # フィールド名と値を辞書オブジェクトに格納
    pattern = r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))'
    ans = dict(re.findall(pattern, template[0], re.MULTILINE + re.DOTALL))

    dic = defaultdict()

    for k, v in ans.items():
        dic[k] = remove_markup(v)

    for k, v in dic.items():
        print(k + ': ' + v)

if __name__ == '__main__':
    main()