def add_char(x):
    lis = []
    c = x.replace(',', '').replace('.', '')
    c = c.split()
    for i in c:
        lis.append(len(i))

    return lis


def main():
    c = add_char("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.")
    print(c)


if __name__ == '__main__':
    main()
