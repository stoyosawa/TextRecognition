## README

<a style="float: right;" href="./README.jp.md"><img src="https://www.worldometers.info/img/flags/ja-flag.gif" width="50">日本語版</a>

The Tensorflow/Keras scripts in this directory recognize handwritten digits (0 to 9).　They use the 60,000 sets of training data and 10,000 sets of test data from [THE MNIST (Modified NIST) DATABASE of handwritten digits](http://yann.lecun.com/exdb/mnist/).

Tested on Tensorflow 2.9.1. The


#### [E_2_1.py](./E_2_1.py)

Download the MNIST dataset, a construct Neural-Network model, and train the model using the dataset. The data is automatically downloaded and saved as `$HOME/.keras/mnist.npz` (numpy zip file).

The model is shown below:

```
Model: "sequential"
_________________________________________________________________
 Layer (type)                  Output Shape              Param #
=================================================================
 conv2d (Conv2D)               (None, 26, 26, 32)        320
 conv2d_1 (Conv2D)             (None, 24, 24, 64)        18496
 max_pooling2d (MaxPooling2D)  (None, 12, 12, 64)        0
 dropout (Dropout)             (None, 12, 12, 64)        0
 flatten (Flatten)             (None, 9216)              0
 dense (Dense)                 (None, 128)               1179776
 dropout_1 (Dropout)           (None, 128)               0
 dense_1 (Dense)               (None, 10)                1290
=================================================================
Total params: 1,199,882
Trainable params: 1,199,882
Non-trainable params: 0
```

The constructed model (architecture) and weights are saved under the `./mnist_model_v2` directory. Refer to the Keras documentation, [Serialization and saving](https://keras.io/guides/serialization_and_saving/), for further information.


#### [E_2_2.py](./E_2_2.py)

A handwritten digits recognition script. Just draw strokes on the 300x300 window using your mouse (left-button press), then hit `Enter`. The predicted number is shown in the top-left region. The number and its probability are shown on the console (command prompt). Enter `ESC` to clear the window. `Q` to quit.

<img src="./images/sample.png" width=150></img>

```
C:\temp>python E_2_2.py
Loaded.
Found 1. Probability 0.9986
Found 3. Probability 1.0000
```

#### [nist_data.py](./nist_data.py)

Test-reads the MNIST dataset file (numpy zip file) and parses it. It then randomly shows 10 images and its associated number on the window. The data is from the test (`x_test` and `y_test`). As the script outputs, the MNIST file contains 60,000 training data and 10,000 test data. The image size is 28x28.

```
C:\temp>python nist_data.py
x_test: (10000, 28, 28)                                  # 28x28の画像が10,000個
x_train: (60000, 28, 28)                                 # 28x28の画像が60,000個
y_train: (60000,)                                        # 数値60,000個
y_test: (10000,)                                         # 数値10,000個
```

#### [eval_model.py](./eval_model.py)

A script to check the accuracy of the model (from `E_2_1.py`). It tries all the 10,000 data from `x_test` and `y_test`. It may take long.

```
C:\temp>python eval_model.py
Model loaded.
NNIST test data loaded.
..................................................................................
..................  Completed in 425.687 seconds. 42.569 samples/ms.
Tested with 10000 samples. Hit rate: 0.989.
```

#### [test_model.py](./test_model.py)

Another test. It randomly picks the test data and feeds it to the model. The target image is shown on the window, and the results are shown on the console. Press ESC to quit. Use any other key to continue the test.

```
C:\temp>python test_model.py
DNN model loaded.
Image data loaded.
Test started. Press ESC to quit. Any other key to continue.
Index: 6499. The answer: 2 >> Predicted: 2, p=1.000.
Index: 9849. The answer: 2 >> Predicted: 2, p=1.000.
Index: 3690. The answer: 6 >> Predicted: 6, p=1.000.
Index: 7304. The answer: 5 >> Predicted: 5, p=1.000.
Index: 8951. The answer: 0 >> Predicted: 0, p=1.000.
Done
```

#### [to_categorical.py](./to_categorical.py)

Just a personal test/practice script (for [tf.keras.utils.to_categorical()](https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical)). No practical purpose.
