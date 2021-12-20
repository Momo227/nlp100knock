import pandas as pd

def main():
    data = pd.read_csv("../../data/popular-names.txt", delimiter='\t', names=['name', 'sex', 'data1', 'data2'])

    data.to_csv('../../data/col1.txt', columns=['name'], header=None, index=False)
    data.to_csv('../../data/col2.txt', columns=['sex'], header=None, index=False)

if __name__ == '__main__':
    main()



