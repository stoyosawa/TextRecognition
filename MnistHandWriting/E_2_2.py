#!/usr/bin/env python

# Suppress CUDA warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
# tf.get_logger().setLevel('ERROR')

import cv2
import numpy as np
import tensorflow as tf


def mouse_wrapper(win_name, img):
    '''Mouse event wrapper.'''

    def on_mouse(event, x, y, flags, param):
        if flags == cv2.EVENT_FLAG_LBUTTON:                                  # Left-button to draw.
            cv2.circle(img, (x, y), 8, 255, -1)
            cv2.imshow(win_name, img)

    return on_mouse


def find_number(model, win_name, img):
    '''Predict the number entered'''

    ''' Deprecated
    blob = cv2.dnn.blobFromImage(img, 1/255, size=(28, 28))    # 画像をblobに変換
    net.setInput(blob)                                         # blobを入力層にセット
    pred = net.forward()                                       # 入力に対する出力を計算
    _, max_val, _, max_loc = cv2.minMaxLoc(pred)               # 出力の最大値を求める
    '''

    blob = cv2.resize(img, (28, 28))
    blob = blob.reshape(1, 28, 28, 1)
    blob = blob.astype(np.float32) / 255
    preds = model.predict(blob, verbose=0)                                   # Returns a list of list containing 10 probabilities.
    num = np.argmax(preds)
    probability = preds[0][num]
    print(f'Found {num}. Probability {probability:.4f}')

    cv2.rectangle(img, (0, 0), (60, 60), 255, -1)                            # Paint the top-left corner in white. The area for putting the predicted number.
    cv2.putText(img, str(num), (10, 50), cv2.FONT_HERSHEY_TRIPLEX, 2, 0, 2)  # Put the number.
    cv2.imshow(win_name, img)                                                # Show me what you've got.



if __name__ == '__main__':
    # Load NN model and weight
    # net = cv2.dnn.readNet('model/mnist_model_sample.pb')                   # deprecated.
    model = tf.keras.models.load_model('mnist_model_v2')
    print('Loaded.')

    # Canvas window for writing numbers (using mousse)
    img = np.zeros((300, 300), np.uint8)
    win_name = 'MNIST'

    cv2.namedWindow(win_name)
    cv2.setMouseCallback(win_name, mouse_wrapper(win_name, img))

    while True:
        cv2.imshow(win_name, img)
        key = cv2.waitKey(0)
        if key == 13:                                                        # Enter. Perform prediction.
            find_number(model, win_name, img)
        elif key == 27:                                                      # Escape. clear the image.
            img.fill(0)
        elif key == 'Q' or 'q':                                              # Q/q. Quit.
            break

    cv2.destroyWindow(win_name)
