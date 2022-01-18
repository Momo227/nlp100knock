import pandas as pd

def main():
    data = pd.read_csv("../../data/popular-names.txt", delimiter='\t', names=['name', "sex", "data", "year"])

    sorted_data = data.sort_values('data', ascending=False)
    print(sorted_data)



if __name__ == '__main__':
    main()



