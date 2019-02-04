from math import floor

def twirl(matr):
    ret_matr = []
    for i in range(len(matr)):
        ret_matr.append([matr[3][i],matr[2][i],matr[1][i],matr[0][i]])
    return ret_matr

def set_key(ex_matr):
    key = {1: 0, 2: 0, 3: 0, 4: 0}

    for row in ex_matr:
        print(row)
    for i in range(1, 5):
        position = int(input("Specify the location of the number " + str(i) + " in the matrix: "))
        key[i] = position

    return key

def encode():
    ex_matr = [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]
    key = set_key(ex_matr)
    msg = input("Input your text: ")
    out_str = ''

    if len(msg)%16 != 0:
        msg += '*' * (16 - (len(msg) % 16))

    for i in range(len(msg)//16):
        text = msg[i*16:(i+1)*16]
        for i in range(0, len(text), len(ex_matr)):
            tmp_str = text[i:i + len(ex_matr)]

            for i in range(len(tmp_str)):
                ex_matr[key[i + 1] // len(ex_matr)][key[i + 1] % 4] = tmp_str[i]
            ex_matr = twirl(ex_matr)

        crypto_str = ''

        for row in ex_matr:
            print(row)
            crypto_str += ''.join(row)
        out_str +=crypto_str
    return out_str

def decode(msg):
    ex_matr = [['0', '1', '2', '3'], ['4', '5', '6', '7'], ['8', '9', '10', '11'], ['12', '13', '14', '15']]
    key = set_key(ex_matr)
    out_str = ''

    for i in range(len(msg) // 16):
        text = msg[i * 16:(i + 1) * 16]
        for i in range(0, len(text), len(ex_matr)):
            tmp_str = text[i:i + len(ex_matr)]
            for j in range(len(tmp_str)):
                ex_matr[i//len(ex_matr)][j] = tmp_str[j]

        print("Матрица  ")
        for iu in ex_matr:
            print(iu)
        decode_str = ''
        for _ in range(4):
            dec_str = ''
            for i in range(len(key)):
                dec_str+=ex_matr[key[i + 1] // len(ex_matr)][key[i + 1] % 4]
            ex_matr = twirl(ex_matr)
            decode_str+=dec_str
        out_str+=decode_str

    out_str = out_str.replace('*', '')
    return out_str


if __name__ == '__main__':
    crypto_text = encode()
    print("Encode text : ", crypto_text)
    print("Decode text : ", decode(crypto_text))