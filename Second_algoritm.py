def encode(keyword):

    list_of_ind = [" " for _ in range(len(keyword))]
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    val = 1
    crypto_str = ''

    for liter in alphabet:
        for j in range(len(keyword)):
            if keyword[j] == liter:
                list_of_ind[j] = val
                val += 1

    text = input("Input text: ")

    if len(text) % len(keyword) != 0:
        for i in range(1, (len(text) % len(keyword))):
            text += '*'

    for i in range(0, len(text), len(keyword)):
        tmp_str = text[i:i + len(keyword)]
        ind_str = ''

        for j in range(0, len(keyword)):
            try:
                ind_str += tmp_str[list_of_ind.index(j+1)]
            except IndexError:
                if len(tmp_str) != len(keyword):
                    tmp_str+="*"*(len(keyword)-len(tmp_str))

        crypto_str += ind_str

    return crypto_str

def decode(text):
    keyword = input("Input keyword: ")
    list_of_ind = [" " for _ in range(len(keyword))]
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    val = 1
    decode_str = ''

    for liter in alphabet:
        for j in range(len(keyword)):
            if keyword[j] == liter:
                list_of_ind[j] = val
                val += 1

    for i in range(0, len(text), len(keyword)):
        tmp_str = text[i:i + len(keyword)]
        ind_str = ''

        for j in list_of_ind:
            ind_str+=tmp_str[j-1]

        decode_str+=ind_str

    decode_str = decode_str.replace('*', '')
    return decode_str


if __name__ == '__main__':
    keyword = input("Input keyword: ")
    msg = encode(keyword)
    print("Encrypt msg - ", msg)
    print("Decrypt msg - ", decode(msg))


