#!/usr/bin/python
# -*- Coding: utf-8 -*-

def re_value(a):
    # # 文字列を逆に出力する
    # re_a_list = list(reversed(a))
    #
    # # listにて表示
    # print(re_a_list)
    #
    # # ''と空白を削除
    # re_a = ''.join(list(reversed(a)))
    #
    # return re_a
    return a[::-1]

def main():
    value = re_value("stress")
    print(value)


if __name__ == '__main__':
    main()
