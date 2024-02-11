
website_url = "" # Replace later with portfolio website link when done.

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

'''
index
y = 24
l = 11
24 % 13 = 11, which is what we want
'''

def printIntro():
    print("\nROT13 Cipher, by Nithin Rajesh " + website_url + "\n\n")

def encrypt_or_decrypt_message(message):
    encrypted_message = ""
    for letter in message:
        letter = letter.upper()
        if(letter in alphabet):
            if(alphabet.index(letter) + 13 >= len(alphabet)):
                encrypted_message += alphabet[alphabet.index(letter) + 13 - len(alphabet)]
            else:
                encrypted_message += alphabet[(alphabet.index(letter) + 13)]
        else:
            encrypted_message += letter
    return encrypted_message
