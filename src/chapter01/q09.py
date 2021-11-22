import re
def cipher(sentence):
    ans = []
    for word in sentence:
        if re.search(r'[a-z]', word):
            ans.append(chr(219-ord(word)))
        else:
            ans.append(word)

    return ''.join(ans)

def main():
    ans1 = cipher('Oh, I have had such a curious dream!')
    print('暗号化:', ans1)
    ans2 = cipher(ans1)
    print('復号化:', ans2)

if __name__ == '__main__':
    main()
