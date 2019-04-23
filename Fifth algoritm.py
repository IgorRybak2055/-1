import string

alphabet = list(string.ascii_lowercase)

def encode(key,text):
    encode_str = ''

    for litter in text:
        litter_ind = alphabet.index(litter.lower())
        new_litter_ind = (litter_ind*key)%26
        encode_str += alphabet[new_litter_ind]

    return encode_str

def decode(text, key):
    decode_str = ''
    # key = int(input("Input key: "))

    for litter in text:
        litter_ind = alphabet.index(litter.lower())
        new_litter_ind = (litter_ind * key) % 26
        decode_str += alphabet[new_litter_ind]

    return decode_str

if __name__ == '__main__':
    key, second_key= int(input("Input key: ")) , int(input("Input second key: "))
    while ((key*second_key)%26 != 1):
        print(" Wrong keys!!! Input the correct keys.")
        key, second_key = int(input("Input key: ")), int(input("Input second key: "))
    text = input("Input text: ")
    crypto_text = encode(key, text)
    print("Encode text - ", crypto_text)

    print("Decode text - ", decode(crypto_text, second_key))