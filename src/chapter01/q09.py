import random

def typoglycemia(sentence):

    sentence = sentence.split(' ')

    if len(sentence) == 4:
        return sentence

    else:
        middle = sentence[1:-1]
        random.shuffle(middle)
        return [sentence[0]] + middle + [sentence[-1]]


def main():
    ans = typoglycemia("I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind.")
    print(ans)

if __name__ == '__main__':
    main()
