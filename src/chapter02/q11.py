import pandas as pd
import csv

def load_data(file_path):
    rows = []
    with open(file_path) as f:
        for row in f:
            row = row.strip().replace("\t"," ")
            rows.append(row)

    return rows


def main():
    data = load_data("../../data/popular-names.txt")

    print(data)



if __name__ == '__main__':
    main()



