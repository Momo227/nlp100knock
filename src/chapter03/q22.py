import pandas as pd


def main():
    data = pd.read_json('../../data/jawiki-country.json', lines=True)

    bretian = data[data['title'] == "イギリス"]

    content = pd.DataFrame(bretian["text"]).reset_index().values.tolist()[0]

    text = content[1].split("\n")

    for mini in text:
        if "[Category:" in mini:
            mini = mini.replace("[[Category:", "").replace("]", "")
            print(mini)





if __name__ == '__main__':
    main()
