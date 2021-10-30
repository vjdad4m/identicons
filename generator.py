#!/usr/bin/env python3
import random
from PIL import Image
import numpy as np
import hashlib
import json
import sys

def generate(WIDTH, HEIGHT):
    # Generate random rgb
    pixelR = int(random.randrange(0, 255))
    pixelG = int(random.randrange(0, 255))
    pixelB = int(random.randrange(0, 255))

    color_fg = (pixelR, pixelG, pixelB)

    # Choose "dark" or "light" background color based on the average color value
    if sum(color_fg) < (3 * 255 / 2):
        color_bg = (255, 255, 255)
    else:
        color_bg = [0, 0, 0]

    color_select = [color_fg, color_bg]

    img_array = []
    for x in range(HEIGHT):
        row = []
        for y in range(WIDTH // 2):
            row.append(random.choice(color_select))
        img_array.append(row + row[::-1])

    return img_array

def main():
    width, height = map(int, input("Enter width and height (separated by spaces): ").split())
    if width < 2 or height < 1 or width % 2 != 0:
        print("[ERROR]: Incorrect dimensions.")
        sys.exit(1)

    n_combs = int(255 * 255 * 255 * width / 2 * height)
    print(f"-> There are {n_combs:,} unique combinations. The chance of generating the same combination is {1/n_combs*100:.20f}%")
    n_imgs = int(input("How many images would you like to generate? "))

    for ix in range(n_imgs):
        img_arr = generate(width, height)
        # Get unique hash
        hash = hashlib.sha256(str(json.dumps(img_arr)).encode('utf-8')).hexdigest()
        img = Image.fromarray(np.array(img_arr).astype(np.uint8))
        img.save(f'./out/{hash}.png')
    
    print(f"Generated {n_imgs} images. Saved to './out/'")

if __name__ == '__main__':
    main()