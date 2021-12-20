import pandas as pd

def main():
    data = pd.read_csv("../../data/popular-names.txt", delimiter='\t', names=['name', "data1", "data2", "data3"])
    name = data["name"].to_list()

    name = set(name)

    print(len(name))


if __name__ == '__main__':
    main()



