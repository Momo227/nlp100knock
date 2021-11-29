import pandas as pd
import glob

def main():
    name = pd.read_csv("../../data/col1.txt", names=['name'])
    sex = pd.read_csv("../../data/col2.txt", names=['sex'])

    df = name.join([sex])

    df.to_csv("../../data/marge_data", index = False, sep='\t', header=None)

if __name__ == '__main__':
    main()



