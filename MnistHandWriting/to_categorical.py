#!/usr/bin/env python
# 2022-05-26: to_categorical

'''
Convert a vector to ont-hot format (just a test)
'''

# これを先に
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import random
import numpy as np
import tensorflow as tf


def categorical_by_tf(numbers):
    return tf.keras.utils.to_categorical(
        a,
        num_classes=None,                                # クラスの数 (None := max(y)+1)
        dtype=np.uint8                                    # dtype
    )


def categorical_by_hand(numbers):
    '''Manually'''
    max_num = max(numbers)
    categorical = np.zeros((len(numbers), max_num+1), dtype=np.uint8)
    for idx, number in enumerate(numbers):
        categorical[idx][number] = 1
    return categorical


if __name__ == '__main__':
    print(f'Tensorflow version: {tf.__version__}')
    
    # Generate a random list
    a = [random.randrange(10) for i in range(20)]

    print('TF:\n', categorical_by_tf(a))
    print('Me:\n', categorical_by_hand(a))
