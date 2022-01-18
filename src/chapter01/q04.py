from collections import defaultdict


def add_char(x):
    dic = defaultdict(int)
    c = x.replace(',', '').replace('.', '')
    c = c.split()
    moji = [0, 4, 5, 6, 7, 8, 14, 15, 18]
    cnt = 0
    for i in c:
        if cnt >= 20:
            break
        if cnt in moji:
            key = i[0]
            dic[key] = cnt + 1
            cnt += 1
        else:
            key = i[0:2]
            key = ''.join(key)
            dic[key] = cnt + 1
            cnt += 1
    return dic


def main():
    c = add_char("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.")
    print(c)


if __name__ == '__main__':
    main()
