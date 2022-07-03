from PIL import Image
from translation_tools import binary_to_text

def decode_pix(pix:int) -> str:
    if pix % 2 == 0: return "0"
    else: return "1"

def decode_img(img_path):
    img = Image.open(img_path)
    binary_message = []

    finished_message = False
    i = 0
    while finished_message == False:
        byte = ""
        pix = list(img.getpixel((i*3+1,0)))
        print(list(img.getpixel((i*3+1,0))), list(img.getpixel((i*3+2,0))), list(img.getpixel((i*3+2,0))))
        for j in range(0, 3):
            byte += decode_pix(pix[j])
        
        pix = list(img.getpixel((i*3+2,0)))
        for j in range(0, 3):
            byte += decode_pix(pix[j])

        pix = list(img.getpixel((i*3+3,0)))
        for j in range(0, 2):
            byte += decode_pix(pix[j])
        
        i += 1
        if decode_pix(pix[2]) == "1": finished_message = True
        binary_message.append(byte)
    
    print(binary_message)
    print(binary_to_text(binary_message))

decode_img("/media/miquel/586A14166A13EF8C/Users/mique/datos_portatil/programar/activo/pysteganography/encripted_file.png")