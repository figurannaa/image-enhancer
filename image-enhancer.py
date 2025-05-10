import argparse
import os
from PIL import Image

parser = argparse.ArgumentParser()

parser.add_argument('-w', '--width', type=int, default=0, help="Provide the desired width in px")
parser.add_argument('-H', '--height', type=int, default=0, help="Provide the desired height in px")
parser.add_argument('-p', '--path', required=True, help="Provide the path to the image")

args = parser.parse_args()

width = args.width
height = args.height
path = args.path

#
# COLORED PRINT
#
def colorMsg(msg): 
    print('\x1b[6;30;42m' + msg + '\x1b[0m')

def colorErr(err): 
    print('\x1b[6;30;41m' + err + '\x1b[0m')

#
# PRECHECKS
#
def check_image(path): 
    print('Checkig if image exsists...')

    if not os.path.isfile(path):
        colorErr("Image not found")
        return False

    try:
        with Image.open(path) as img:
            img.verify()  


            return True
    except:
        colorErr(f"The file at '{path}' is not a valid image")
        return False

def adjust_size(image_path, width, height):
    with Image.open(image_path) as img:
        og_width, og_height = img.size

        if width == 0 and height == 0:
            print(f"Using original sizes: {og_width}px x {og_height}px")
            return og_width, og_height

        if width == 0:
            width = int((height / og_height) * og_width)
            print(f"Calculated width: {width}px (original was {og_width}px)")

        if height == 0:
            height = int((width / og_width) * og_height)
            print(f"Calculated height: {height}px (original was {og_height}px)")

        return width, height

#
# RESIZE
#
def resize_image(image_path, width, height, output_path=None):
    with Image.open(image_path) as img:
        resized_img = img.resize((width, height), Image.LANCZOS)  
        save_path = output_path if output_path else image_path  
        resized_img.save(save_path)
        print(f"Image saved to {save_path} with size {width}x{height}")

#
# MAIN
#
colorMsg("Image enhancing started...")

if not check_image(path):
    exit(1)

width, height = adjust_size(path, width, height)

resize_image(path, width, height, output_path='resized_' + os.path.basename(path))

colorMsg("Image enhancing is finished...")