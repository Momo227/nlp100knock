import pandas as pd
import re

def main():
    data = pd.read_json('../../data/jawiki-country.json', lines=True)

    bretian = data[data['title'] == "イギリス"]

    content = pd.DataFrame(bretian["text"]).reset_index().values.tolist()[0]

    text = content[1].split("\n")

    for mini in text:
        res = re.search("^====", mini)
        if res != None:
            print(mini + str(3))
        else:
            res = re.search("^===", mini)
            if res != None:
                print(mini+ str(2))
            else:
                res = re.search("^==", mini)
                if res != None:
                    print(mini+ str(1))





if __name__ == '__main__':
    main()
