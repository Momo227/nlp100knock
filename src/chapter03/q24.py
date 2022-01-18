import pandas as pd
import re

def main():
    data = pd.read_json('../../data/jawiki-country.json', lines=True)

    bretian = data[data['title'] == "イギリス"]

    content = pd.DataFrame(bretian["text"]).reset_index().values.tolist()[0]

    text = content[1].split("\n")

    pattern = re.compile('File|ファイル:(.+?)\|')

    for row in text:
        file = re.findall(pattern, row)
        if file:
            print (file[0])


if __name__ == '__main__':
    main()
