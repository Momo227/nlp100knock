#!/usr/bin/python
# -*- Coding: utf-8 -*-

def add_char(x):

    return x[::2]
    

def main():
    c = add_char("パタトクカシーー")
    print(c)


if __name__ == '__main__':
    main()
