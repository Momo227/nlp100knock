import sys
def load_data(file_path):
    rows = []
    with open(file_path) as f:
        for row in f:
            row = row.strip().replace("\t"," ")
            rows.append(row)

    return rows

def main():
    args = sys.argv

    num = args[1]

    num = int(num)

    data = load_data("../../data/popular-names.txt")

    zenhan = []
    for i in range(num):
        zenhan.append(data[i])

    kouhan = []
    for i in range(num, len(data)):
        kouhan.append(data[i])

    print("前半\n")
    print(zenhan)
    print("\n後半\n")
    print(kouhan)

if __name__ == '__main__':
    main()

# python q16.py N (Nに任意の自然数)



