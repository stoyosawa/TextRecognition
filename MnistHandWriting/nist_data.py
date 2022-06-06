#!/usr/bin/env python

import os
import random
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw

FILE = os.path.expanduser('~/.keras/datasets/mnist.npz') # NIST data file
FONT = 'C:/Windows/Fonts/Arial.ttf'

class NistData:
    '''
    Read the NIST Handwriting dataset (mnist.npz) loaded through tensorflow.keras.datasets.mnist.mnist.load_data().
    It contains four files (ndarrays): images (28x28) and its number (0-9) for training and testing.
    The code is for understanding the dataset. No practical purpose.
    '''
    def __init__(self, file=FILE):
        nist = np.load(FILE)                             # Read the NIST file (npz format)
        self.npz_file = file
        self.files = nist.files
        self.nd = {file:nist[file] for file in self.files}

        # For drawing
        self.font = ImageFont.truetype(FONT, size=18)    # 18 points = 24 pixels on Windows (the handwritten letters is 28x28)


    def __getitem__(self, key):
        return self.nd[key]


    def get_files(self):
        return self.files


    def size(self, key):
        '''Retruns the number of elements in the key (e.g., x_train has 60,000 elements).'''
        return self[key].shape[0]

    def get_image(self, index=0, category='train'):
        '''Returns the image and the answer'''
        img = self[f'x_{category}'][index]
        answer = self[f'y_{category}'][index]
        return (img, answer)


    def get_image_with_answer(self, index=0, category='train'):
        '''Create an image with the sample and answer side-by-side. For testing.'''
        img, answer = self.get_image(index, category)

        # Pillow for a reasonable fort.
        h, w = img.shape
        canvas = Image.new('RGB', (w*2,  h), 'black')
        canvas.paste(Image.fromarray(img))
        d = ImageDraw.Draw(canvas)
        d.text((w*3//2, h//2), str(answer), font=self.font, fill='lime', anchor='mm')

        return np.array(canvas)


if __name__ == '__main__':
    nist_data = NistData()
    for file in nist_data.get_files():
        print(f'{file}: {nist_data[file].shape}')

    # Randomly show sample images. The answer appears on the window title bar.
    for i in range(10):
        canvas = nist_data.get_image_with_answer(index=random.randrange(nist_data.size('x_train')))
        cv2.imshow('NIST', canvas)
        cv2.waitKey(1000)
