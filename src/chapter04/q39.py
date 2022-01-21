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


def main():
    datas = []
    with open("../../data/neko.txt.mecab") as input_file:
        for row in input_file:
            line = make_dict(row)
            if line != "pas":
                datas.append(make_dict(row))

    ans = defaultdict(int)
    for lis in datas:
        for part in lis:
            k, v = part
            if k == 'base':
                word = v
            if k == 'pos' and v != "記号":
                ans[word] += 1

    ans = sorted(ans.items(), key=lambda x:x[1], reverse=True)

    ranks = [r + 1 for r in range(len(ans))]
    values = [a[1] for a in ans]
    plt.figure(figsize=(8, 4))
    plt.scatter(ranks, values)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('出現頻度順位')
    plt.ylabel('出現頻度')
    plt.show()


if __name__ == '__main__':
    main()
