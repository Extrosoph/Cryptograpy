#Originally wrote by Russell Ballestrini
#edited by Jin Hong and Theo Andily

from random import shuffle
from string import ascii_letters, digits
from collections import OrderedDict


def random_monoalpha_cipher(pool=None):
    """Generate a Monoalphabetic Cipher
       Returns a dictionary of substitution table randomly generated
    """
    if pool is None:
        pool = ascii_letters + digits
    original_pool = list(pool)
    shuffled_pool = list(pool)
    shuffle(shuffled_pool)
    return dict(zip(original_pool, shuffled_pool))

def key_monoalpha_cipher(key):
    """Generate a Monoalphabetic Cipher using the key provided
       Returns a dictionary of substitution table using the key
    """
    key = "".join(OrderedDict.fromkeys(key))
    pool = ascii_letters + digits
    for char in ascii_letters:
        if char == key[-1]:
            for i in range((pool.index(char))+1, len(pool)):
                if pool[i] in key:
                    continue
                else:
                    key += pool[i]

    for char in ascii_letters:
        if char not in key:
            key += char
    return dict(zip(pool, key))

def inverse_monoalpha_cipher(monoalpha_cipher):
    """Given a Monoalphabetic Cipher (dictionary) return the inverse."""
    inverse_monoalpha = {}
    for key, value in monoalpha_cipher.items():
        inverse_monoalpha[value] = key
    return inverse_monoalpha

def encrypt_with_monoalpha(message, monoalpha_cipher):
    """Encrypts message using the substitution table monoalpha_cipher"""
    encrypted_message = []
    for letter in message:
        encrypted_message.append(monoalpha_cipher.get(letter, letter))
    return ''.join(encrypted_message)

def decrypt_with_monoalpha(encrypted_message, monoalpha_cipher):
    """Decrypts message using the substitution table monoalpha_cipher"""
    return encrypt_with_monoalpha(
               encrypted_message,
               inverse_monoalpha_cipher(monoalpha_cipher)
           )


#Example usage
print(ascii_letters)
message = 'secret message'
cipher = key_monoalpha_cipher('monopoly')
ciphertext = encrypt_with_monoalpha(message, cipher)
print(ciphertext)
plaintext = decrypt_with_monoalpha(ciphertext, cipher)
print(plaintext)