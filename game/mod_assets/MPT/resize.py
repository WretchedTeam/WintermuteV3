from PIL import Image
from glob import iglob
import os
import sys
from concurrent.futures import ThreadPoolExecutor

import logging

required_factor = ((960 / 720) * 1080) / 960

def retrieve_png_files(folder: str):
    for i in iglob(f"{folder}/**.png", recursive=True):
        yield i

def factor_resize(image: Image.Image, factor=1.0, **kwargs):
    new_size = tuple(int(v * factor) for v in image.size)
    return image.resize(new_size, **kwargs)

def resize_mpt_component(filename):
    image = Image.open(filename)

    if image.size[0] != 960 and image.size[1] != 960:
        return

    new_image = image.resize((1440, 1440), resample=Image.Resampling.HAMMING)
    new_image.save(filename, quality=100)
    logging.info(f"{filename} done.")

def resize_mpt_folder(folder):
    with ThreadPoolExecutor(5) as executor:
        executor.map(resize_mpt_component, retrieve_png_files(folder))

if __name__ == "__main__":
    os.chdir(sys.path[0])

    logging.basicConfig(filename='resize.log', level=logging.INFO)

    resize_mpt_folder("monika")
    resize_mpt_folder("natsuki")
    resize_mpt_folder("yuri")
    resize_mpt_folder("sayori")
