import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path, sep='\t')
    return data

def main():
    data = load_data("../../data/popular-names.txt")
    print(len(data))


if __name__ == '__main__':
    main()

    # Unixコマンドなら↓
    # wc data/popular-names.txt


