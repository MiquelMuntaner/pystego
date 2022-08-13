from PIL import Image
from tools.translation_tools import binary_to_text

def decode_pix(pix:int) -> str:
    if pix % 2 == 0: return "0"
    else: return "1"

def decode_img(img_path: str) -> str:
    """decode an image that has been encoded with this program

    Args:
        img_path (str): the path of the image you want to decode

    Returns:
        str: The decoded message of the image
    """
    img = Image.open(img_path)
    width, height = img.size
    binary_message = []
    finished_message, i = False, 0
    row = 0

    while finished_message == False:
        byte = ""
        i += 1

        for z in range(1, 3):
            if i*3+z >= width:
                row += 1
                i=0
            pix = list(img.getpixel((i*3+z, row)))
            for j in range(0, 3):
                byte += decode_pix(pix[j])

        if i*3+3 >= width:
                row += 1
                i=0
        pix = list(img.getpixel((i*3+3, row)))
        for j in range(0, 2):
            byte += decode_pix(pix[j])

        if decode_pix(pix[2]) == "1":
            finished_message = True

        binary_message.append(byte)

    return binary_to_text(binary_message)
