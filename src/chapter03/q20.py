import pandas as pd


def main():
    data = pd.read_json('../../data/jawiki-country.json', lines=True)

    bretain = data[data['title'] == "イギリス"]

    print(bretain)

    bretain.to_csv('../../data/bretain.csv', header=["title", "text"], index=False)

if __name__ == '__main__':
    main()
