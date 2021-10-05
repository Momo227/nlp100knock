#!/usr/bin/python
# -*- Coding: utf-8 -*-

def add_char(x, y):
    c = []
    for i in range(len(x)):
        c.append(x[i])
        c.append(y[i])

    return ''.join(c)


def main():
    c = add_char("パトカー", "タクシー")
    print(c)


if __name__ == '__main__':
    main()
