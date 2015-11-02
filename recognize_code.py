from PIL import Image, ImageEnhance
from PIL import ImageDraw, ImageFont, ImageFilter
from pytesseract import image_to_string  # need put pytesseract path into PATH
import os, sys, re

def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

def get_code(name):
    threshold = 140
    table = []
    cur_path = cur_file_dir()
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)

    rep = {'O':'0',
           'I':'1','L':'1',
           'Z':'2',
           'S':'8'
           };
    im = Image.open(name)
    imgry = im.convert('L')
    imgry.save('g'+name)

    out = imgry.point(table, '1')
    out.save('b' + name)

    ff = Image.open('b' + name)

    text = image_to_string(ff)

    text = text.strip()
    text = text.upper()

    for r in rep:
        text = text.replace(r, rep[r])
    print(text)

def get_verfi_code():
    # get current path
    cur_path = cur_file_dir()
    shot_path = "pay.png"
    print(shot_path)

    #crop the verify code image
    im = Image.open(shot_path)
    box = (870, 410, 922, 425)
    region = im.crop(box)
    verify_path = "verify.png"
    region.save(verify_path)
    return verify_path

if __name__ == '__main__':
    verify_path = get_verfi_code()
    get_code(verify_path)
    
