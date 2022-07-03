from PIL import Image
from translation_tools import text_to_binary

def modify_pixel(pix: int, bit: str) -> int:
    if bit == "1" and pix % 2 == 0:
            if pix < 255: pix += 1
            else: pix -= 1
    elif bit == "0" and pix % 2 != 0:
            if pix < 255: pix += 1
            else: pix -= 1
    
    return pix

def encode_img(img_path, text, new_file_name):
    img = Image.open(img_path)
    binary_text = text_to_binary(text)
    len_data = len(binary_text)

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
        
        
        if len_data == idx+1 and pix[2] % 2 == 0:
            if pix[2] < 255: pix[2] += 1
            else: pix[2] -= 1
        elif len_data > idx+1 and pix[2] % 2 != 0:
            if pix[2] < 255: pix[2] += 1
            else: pix[2] -= 1
        
        img.putpixel((idx*3+3,0), tuple(pix))
        img.save(new_file_name)

    


encode_img("/media/miquel/586A14166A13EF8C/Users/mique/datos_portatil/programar/activo/pysteganography/pysteganography/test.png", "Esto es una prueba", "encripted_file.png")