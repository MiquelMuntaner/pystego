
def text_to_binary(text:str) -> list:
    binary = [bin(char).replace("0b", "") for char in [ord(char) for char in text]]
    return ["0"*(8-len(byte)) + byte for byte in binary if len(byte) < 8]

def binary_to_text(binary:list) -> str:
    return "".join([chr(int(byte, 2)) for byte in binary])