#!/usr/bin/env python
# 2022-05-26: Testing the MNIST model

# Run this first to suppress CUDA warnings.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


import random
import cv2
import numpy as np
import tensorflow as tf
from nist_data import NistData


if __name__ == '__main__':
    # Load the pre-built model.
    model = tf.keras.models.load_model('mnist_model_v2')
    print('DNN model loaded.')

    # Load the NIST data
    ndata = NistData()
    print('Image data loaded.')
    print('Test started. Press ESC to quit. Any other key to continue.')

    # Randomly pick the image from the NIST data.
    while True:
        idx = random.randrange(ndata.size('x_test'))
        img, answer = ndata.get_image(idx, category='test')
        cv2.imshow('Sample', img)

        # reshape the image and predict
        img = img.reshape(1, 28, 28, 1)
        img = img.astype(np.float32) / 255
        preds = model.predict(img, verbose=0)            # a list of a list of 10 elements: [ [p0, p1, p2, ..., p9] ]
        num = np.argmax(preds)
        
        print(f'Index: {idx}. The answer: {answer} >> Predicted: {num}, p={preds[0][num]:.3f}.')

        if cv2.waitKey() == 27:
            break

    print('Done')
