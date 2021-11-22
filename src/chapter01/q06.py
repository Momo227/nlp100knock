def char_bi_gram(x):
    c = x.replace(',', '').replace('.', '')
    c = c.split()
    ans = []
    for i in c:
        if len(i) == 1:
            mini_ans = []
            mini_ans.append(i)
            mini_ans.append(" ")
            ans.append(mini_ans)
        else:
            mini_ans = []
            mini_ans.append(" ")
            mini_ans.append(i[0])
            if mini_ans not in ans:
               ans.append(mini_ans)
            for j in range(len(i) - 1):
                mini_ans = []
                mini_ans.append(i[j])
                mini_ans.append(i[j+1])
                if mini_ans in ans:
                    continue
                ans.append(mini_ans)
            mini_ans = []
            mini_ans.append(i[len(i) - 1])
            mini_ans.append(" ")
            ans.append(mini_ans)

    del ans[-1]

    if len(c[0]) != 1:
        del ans[0]

    return ans

def make_wa(x, y):
    ans = []

    for i in range(len(x)):
        if x[i] not in ans:
            ans.append(x[i])
        else:
            continue

    for i in range(len(y)):
        if y[i] not in ans:
            ans.append(y[i])
        else:
            continue

    return ans

def make_seki(x, y):
    ans = []

    for i in range(len(x)):
        if (x[i] in x) and (x[i] in y):
            if x[i] not in ans:
                ans.append(x[i])
            else:
                continue
        else:
            continue

    for i in range(len(y)):
        if (y[i] in x) and (y[i] in y):
            if y[i] not in ans:
                ans.append(y[i])
            else:
                continue
        else:
            continue

    return ans

def make_sa(x, y):
    x = set(map(tuple, x))
    y = set(map(tuple, y))
    ans = x.difference(y)

    return ans

def main():
    X = char_bi_gram("paraparaparadise")
    Y = char_bi_gram("paragraph")


    wa = make_wa(X, Y)
    print("和集合 : " + str(wa) + "\n")

    seki = make_seki(X, Y)
    print("積集合 : " + str(seki) + "\n")

    sa = make_sa(X, Y)
    print("差集合 : " + str(sa) + "\n")

    se = char_bi_gram("se")

    if se[0] in X:
        print("X:Yes")
    else:
        print("X:No")

    if se[0] in Y:
        print("Y:Yes")
    else:
        print("Y:No")


if __name__ == '__main__':
    main()