from collections import defaultdict
import re
import matplotlib.pyplot as plt
import japanize_matplotlib


def make_dict(data):
    elements = re.split('[\t,\n]', data)

    line = defaultdict(str)

    if elements[0] == "EOS" or elements[0] == "":
        line = "pas"
        return line

    if 0 < len(elements) < 4:
        line["surface"] = elements[0]
        line["base"] = ""
        line["pos"] = ""
        line["pos1"] = ""
        return line.items()
    else:
        line["surface"] = elements[0]
        line["base"] = elements[7]
        line["pos"] = elements[1]
        line["pos1"] = elements[5]
        return line.items()

def hindo(path):
    datas = []
    with open(path) as input_file:
        for row in input_file:
            line = make_dict(row)
            if line != "pas":
                datas.append(make_dict(row))

    ans = defaultdict(int)
    for lis in datas:
        for part in lis:
            k, v = part
            if k == 'surface':
                word = v
            if k == 'pos' and v != "記号":
                ans[word] += 1


    return sorted(ans.items(), key=lambda x:x[1], reverse=True)

def main():
    datas = hindo("../../data/neko.txt.mecab")
    keys = [mini[0] for mini in datas[0:10]]
    values = [mini[1] for mini in datas[0:10]]
    plt.figure(figsize=(8, 4))
    plt.bar(keys, values)
    plt.show()

if __name__ == '__main__':
    main()
