#!/usr/bin/python
# -*- Coding: utf-8 -*-

def word_bi_gram(x):
    c = x.replace(',', '').replace('.', '')
    c = c.split()
    ans = []
    for i in range(len(c) - 1):
        ans.append(c[i:i+2])

    return ans
        



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



def main():
    ans1 = word_bi_gram("I am an NLPer")
    ans2 = char_bi_gram("I am an NLPer")
    print("word_bi_gram : " + str(ans1) + "\n")
    print("char_bi_gram : " + str(ans2) + "\n")


if __name__ == '__main__':
    main()
