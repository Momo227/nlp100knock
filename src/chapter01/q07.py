def make_sentence(x, y, z):
    ans1 = str(x) + "時の" + str(y) +  "は" + str(z)
    return ans1

def main():
    ans1 = make_sentence(12, "気温", 22.4)

    print(ans1)

if __name__ == '__main__':
    main()
