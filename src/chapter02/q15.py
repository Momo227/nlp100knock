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

    start = len(data) - num

    for i in range(start, len(data)):
        print(data[i])

if __name__ == '__main__':
    main()

# python q65.py N (Nに任意の自然数)



