#!/usr/bin/env python

# Suppress CUDA warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout
from tensorflow.keras.layers import Flatten, Dense
from tensorflow.keras.optimizers import RMSprop

# Check the TF version
print(f'Tensorflow version {tf.__version__}')


# Read M-NIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(f'Handwritten data read: Train {len(x_train)}, Test {x_test}')


# Reformat the dataset
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)                       # x_train.shape[0] = 60,000
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)                          # x_train.shape[0] = 10,000
x_train = x_train.astype(np.float32) / 255                                   # Black/white int [0, 255] to float [0, 1).
x_test = x_test.astype(np.float32) / 255
y_train = tf.keras.utils.to_categorical(y_train, 10)                         # A vector that denotes the numbers written ([0, 9]). Convert them to 'one-hot'.
y_test = tf.keras.utils.to_categorical(y_test, 10)


# Construct the Neural-network structure (sequential model)
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))        # Rectified Linear Unit
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))


# Compile the model
model.compile(optimizer=RMSprop(), loss='categorical_crossentropy', metrics=['accuracy'])
model.summary()


# Train the model. Reduce epochs=10 when the training takes too much time.
model.fit(x_train, y_train, batch_size=128, epochs=10, validation_data=(x_test, y_test))


# Save the network structure and the weight dataset （in Tensorflow's pb format: keras_metadata.pb and saved_model.pb under the directory)
model.save('mnist_model_v2')


'''The functions are deprecated (were for 2.3.1).

sess = tf.compat.v1.keras.backend.get_session()
tf.identity(model.outputs[0], name='output_node0')
graph = tf.compat.v1.graph_util.convert_variables_to_constants( sess, sess.graph.as_graph_def(), ['output_node0'])
tf.io.write_graph(graph, graph_dir, graph_file, as_text=False)
'''
