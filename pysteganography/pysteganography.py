from tools.encoding import encode_img
from tools.decoding import decode_img
from tools.encryption_tools import encrypt, decrypt
from tools.colors import colors
from tools.interface import interface_tool
from bullet import Password
from pathlib import Path
import os
import typer

app = typer.Typer()

@app.command()
def interface():
    """Use an interface in the terminal to encode and decode images more easily"""
    interface_tool()

@app.command()
def encode(message: str, img_path: Path, encryption: bool = typer.Option(False, "--encrypt", "-e", help="Secure encryption with AES-256 bit algorithm")):
    """Encode a message in an image, you can use AES-256 bit encryption if you use the -e flag"""

    if encryption == False:
        print(colors.fg.yellow, "Warning: you are not using encryption anyone with this program will be able to see the message. To use encryption type -e at the end of the command.", colors.reset)
    else:
        print(colors.fg.darkgrey, "\nRemember that if you lose the password you will lose the message", colors.reset)
        password_match = False
        while password_match == False:
            password = Password(prompt="Type your password: ", hidden="*").launch()
            password2 = Password(prompt="Re-type your password: ", hidden="*").launch()
            password_match = password == password2

            if not password_match: print(colors.fg.red, "\nPasswords don't match", colors.reset)

        message = encrypt(message, password.encode())
    
    encode_img(str(img_path), str(message))
    print(colors.fg.green, colors.bold, "\nThe image has been encrypted", colors.reset)

@app.command()
def decode(img_path: Path, encryption: bool = typer.Option(False, "--encrypted", "-e", help="Secure encryption with AES-256 bit algorithm")):
    message = decode_img(img_path)
    if encryption:
        password = Password(prompt="Type the password (leave empty if there is no password): ", hidden="*").launch()
        message = decrypt(message.replace('b\'', '')[:-1].encode(), password.encode())
        
    print(colors.fg.green, colors.bold, "\nThe message has been decoded:", colors.reset)
    print(message)

if __name__ == "__main__":
    app()