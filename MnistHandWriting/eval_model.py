#!/usr/bin/env python

# Suppress CUDA warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from time import monotonic
import cv2
import numpy as np
import tensorflow as tf
from nist_data import NistData

# Load the pre-built model
model = tf.keras.models.load_model('mnist_model_v2')
print('Model loaded.')

# Read the M-NIST dataset
nist_data = NistData()
n_test = nist_data.size('x_test')
print('NNIST test data loaded.')


# How long does it take?
start = monotonic()                                      # clock time. Includes sleep time.


# Test the model using the test dataset (x_test and y_test)
hit = 0
for idx in range(n_test):
    img, answer = nist_data.get_image(idx, category='test')

    blob = cv2.resize(img, (28, 28))
    blob = blob.reshape(1, 28, 28, 1)
    blob = blob.astype(np.float32) / 255
    preds = model.predict(blob, verbose=0)
    predicted = np.argmax(preds)
    if predicted == answer:
        hit += 1

    # Progress bar as it takes quite a bit to try all the test data (10,000). Every 100 images.
    if idx % 100 == 0:
        print('.', end='', flush=True)

hit_rate = hit / n_test
duration = monotonic() - start
print(f'  Completed in {duration:.3f} seconds. {duration/n_test*1000:.3f} samples/ms.')
print(f'Tested with {n_test} samples. Hit rate: {hit_rate:.3f}.')

