import pandas as pd


def main():
    data = pd.read_json('../../data/jawiki-country.json', lines=True)

    bretain = data[data['title'] == "イギリス"]

    print(bretain)


if __name__ == '__main__':
    main()
