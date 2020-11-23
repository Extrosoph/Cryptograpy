message = "Cipher text goes here"

def decrypt(key, message):
    message = message.upper()
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for letter in message:
        if letter in alpha:
            letter_index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[letter_index]
        else:
            result = result + letter
    return result

def main():

    # Decrypting the message
    for i in range(1, 27):
        print("Key:", i)
        print(decrypt(i, message))

if __name__ == "__main__":
    main()


