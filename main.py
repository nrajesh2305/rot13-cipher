from cipher import *

printIntro()
message = ""

while message != "QUIT":
    message = input("Enter a message to encrypt/decrypt (or QUIT):\n> ")
    if(message == "QUIT"):
        exit()
    else:
        break

print("\nThe translated message is:\n" + encrypt_or_decrypt_message(message) + "\n")
