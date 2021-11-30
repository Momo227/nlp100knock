import json

def main():

    data = []
    decoder = json.JSONDecoder()
    with open('../../data/jawiki-country.json') as f:
        line = f.readline()
        while line:
            data.append(decoder.raw_decode(line))
            line = f.readline()
            if '"title": "イギリス"' in line:
                Britian = line


    print(Britian)

    # イギリスのデータの書き込み
    with open("../../data/Britian.json", "w") as f:
        json.dump(Britian, f, indent=2)


if __name__ == '__main__':
    main()
