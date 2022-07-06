from PIL import Image
from tools.translation_tools import text_to_binary

def modify_pixel(pix: int, bit: str) -> int:
    if bit == "1" and pix % 2 == 0:
            if pix < 255: pix += 1
            else: pix -= 1
    elif bit == "0" and pix % 2 != 0:
            if pix < 255: pix += 1
            else: pix -= 1
    
    return pix

def new_img_name(img_path: str) -> str:
    if "/" in img_path:
        img_path = img_path.split('/')
    elif "\\" in img_path:
        img_path = img_path.split('\\')
    
    filename = img_path[len(img_path)-1].split('.')
    filename[0] += '-encoded'
    return '.'.join(filename)

def encode_img(img_path: str, text:str) -> None:
    """encode a text within an image (steganography)

    Args:
        img_path (str): the path of the image you want to encode
        text (str): the message you want to encode
    """
    img = Image.open(img_path)
    binary_text = text_to_binary(text)
    len_data = len(binary_text)
    new_file_name = new_img_name(img_path)

    for idx, byte in enumerate(binary_text):
        pix = list(img.getpixel((idx*3+1,0)))
        for i in range(0, 3):
            pix[i] = modify_pixel(pix[i], byte[i])
        img.putpixel((idx*3+1,0), tuple(pix))

        pix = list(img.getpixel((idx*3+2,0)))
        for i in range(0, 3):
            pix[i] = modify_pixel(pix[i], byte[i+3])
        img.putpixel((idx*3+2,0), tuple(pix))

        pix = list(img.getpixel((idx*3+3,0)))
        for i in range(0, 2):
            pix[i] = modify_pixel(pix[i], byte[i+6])
        
        if len_data == idx+1:
            pix[2] = modify_pixel(pix[2], "1")
        elif len_data > idx+1:
            pix[2] = modify_pixel(pix[2], "0")
        
        img.putpixel((idx*3+3,0), tuple(pix))
    
    img.save(new_file_name)