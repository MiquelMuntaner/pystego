from tools.encoding import encode_img
from tools.decoding import decode_img
from tools.encryption_tools import encrypt, decrypt
from tools.colors import colors
from bullet import Password
import os

title = colors.fg.green + """
  _____        _____ _                   
 |  __ \      / ____| |                  
 | |__) |   _| (___ | |_ ___  __ _  ___  
 |  ___/ | | |\___ \| __/ _ \/ _` |/ _ \ 
 | |   | |_| |____) | ||  __/ (_| | (_) |
 |_|    \__, |_____/ \__\___|\__, |\___/ 
         __/ |                __/ |      
        |___/                |___/       """ + colors.reset

def interface_tool():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(title)
    print(colors.fg.darkgrey, "\nHide encrypted messages in your photos\nMade by Miquel Muntaner\nGithub repository: https://github.com/MiquelMuntaner/pystego\n", colors.reset)
    print("1. encrypt\n2. decrypt")
    option = input("Choose an option (1 or 2): ")

    if option == "1":
        path = input("\nWrite the path of the image you want to encrypt (.png): ")
        message = input("Write the message you want to encrypt: ")

        print(colors.fg.darkgrey, "\nYou can encrypt your message with a password so that not everyone can see the content using this program\nThis encryption is done with the very secure algorithm AES-256 bits", colors.reset)
        want_password = input("Do you want to use password?(y/n): ")

        if want_password == "y":
            print(colors.fg.darkgrey, "\nRemember that if you lose the password you will lose the message", colors.reset)
            password_match = False
            while password_match == False:
                password = Password(prompt="Type your password: ", hidden="*").launch()
                password2 = Password(prompt="Re-type your password: ", hidden="*").launch()
                password_match = password == password2

                if not password_match: print(colors.fg.red, "\nPasswords don't match", colors.reset)

            message = encrypt(message, password.encode())
        
        encode_img(path, str(message))
        print(colors.fg.green, colors.bold, "\nThe image has been encrypted", colors.reset)
    elif option == "2":
        path = input("\nWrite the path of the image you want to decode (.png): ")
        password = Password(prompt="Type the password (leave empty if there is no password): ", hidden="*").launch()

        message = decode_img(path)

        if len(password) != 0:
            message = decrypt(message.replace('b\'', '')[:-1].encode(), password.encode())

        print(colors.fg.green, colors.bold, "\nThe message has been decoded:", colors.reset)
        print(message)