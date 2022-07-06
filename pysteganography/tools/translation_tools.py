def text_to_binary(text:str) -> list:
    """translates text to binary

    Args:
        text (str): the text you want to translate

    Returns:
        list: the text translated to binary in a list with each byte
    """
    binary = [bin(char).replace("0b", "") for char in [ord(char) for char in text]]
    return ["0"*(8-len(byte)) + byte for byte in binary if len(byte) < 8]

def binary_to_text(binary:list) -> str:
    """translates binary to text

    Args:
        binary (list): a list with each byte in a string

    Returns:
        str: a string with the content already translated
    """
    return "".join([chr(int(byte, 2)) for byte in binary])