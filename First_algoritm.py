import os

def encode(key, text):
    # key, text = int(input("Input key: ")), input("Input your message: ")
    crypto_matr = []
    i = 0
    flag = True

    for _ in range(key):
        crypto_matr.append(["*" for _ in range(len(text))])

    for liter in range(len(text)):
        crypto_matr[i][liter] = text[liter]

        if key - i == 1: flag = False
        if i == 0: flag = True
        i += 1 if flag else -1
    
    # for ind in crypto_matr:
    #     print(ind)

    crypto_str = ''

    for row in crypto_matr:
        for el in row:
            if el != '*':
                crypto_str += el
    # print(crypto_str)
    return crypto_str

def decode(key, text):
    crypto_matr = []
    i = 0
    flag = True
    decrypt_str = ''
    for _ in range(key):
        crypto_matr.append(["*" for _ in range(len(text))])

    for liter in range(len(text)):
        crypto_matr[i][liter] = '#'

        if key - i == 1: flag = False
        if i == 0: flag = True
        i += 1 if flag else -1

    i = 0

    for row in crypto_matr:
        for el in range(len(row)):
            if row[el] == '#':
                row[el] = text[i]
                i+=1
    # for qwe in crypto_matr:
    #     print(qwe)
    i = 0

    for j in range(len(text)):
        decrypt_str += crypto_matr[i][j]

        if key - i == 1: flag = False
        if i == 0: flag = True
        i+=1 if flag else -1

    return decrypt_str


if __name__ == '__main__':
    key, text = int(input("Input key: ")), input("Input your message: ")
    msg = encode(key,text)
    print("Encrypt msg - ",msg )
    print("Decrypt msg - ",decode(key, msg))







