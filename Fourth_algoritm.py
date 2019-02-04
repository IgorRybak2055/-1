import string

alphabet = list(string.ascii_lowercase)

def encode(key,text):
    encode_str = ''

    for litter in text:
        litter_ind = alphabet.index(litter.lower())
        new_litter_ind = (litter_ind+key)%26
        encode_str += alphabet[new_litter_ind]

    return encode_str

def decode(text):
    decode_str = ''
    key = int(input("Input key: "))

    for litter in text:
        litter_ind = alphabet.index(litter.lower())
        new_litter_ind = (litter_ind + 26 - key) % 26
        decode_str += alphabet[new_litter_ind]

    return decode_str

if __name__ == '__main__':
    key , text = int(input("Input key: ")) , input("Input message: ")
    crypto_text = encode(key, text)
    print("Encode text - ", crypto_text)

    print("Decode text - ", decode(crypto_text))