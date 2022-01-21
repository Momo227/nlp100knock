from collections import defaultdict
import re


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


def main():
    datas = []
    with open("../../data/neko.txt.mecab") as input_file:
        for row in input_file:
            line = make_dict(row)
            if line != "pas":
                datas.append(make_dict(row))

    ans = set()
    for i in range(2, len(datas)):
        mini = []
        for part in datas[i-2]:
            k, v = part
            if k == 'surface':
                sub = v
                continue
            if k == 'pos' and v == "名詞":
                mini.append(sub)
        for part in datas[i-1]:
            k, v = part
            if k == 'surface' and v == "の":
                continue
            if k == 'pos' and v == "名詞":
                mini.append("の")
        for part in datas[i]:
            k, v = part
            if k == 'surface':
                sub = v
                continue
            if k == 'pos' and v == "名詞":
                mini.append(sub)
        if len(mini) == 3:
            ans.add(''.join(mini))

    print(ans)


if __name__ == '__main__':
    main()
