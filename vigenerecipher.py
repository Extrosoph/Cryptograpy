
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))



def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


message = 'ZWHIKVYIGB TEL XXEG WHIK BTI AWHIKKDEYB'
key = 'over'
print(originalText(message, key))
