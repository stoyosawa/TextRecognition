## README

The Tensorflow/Keras scripts in this directory recognize handwritten numbers (0 to 9). `E_2_1.py` is for DNN training: It uses the MNIST handwritten datasets. `E_2_2.py` is a user proguram that performs actual recognitions. They were first implemented for Section E.2 手書き数字推定モデル in [実践OpenCV 4 for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html). The codes here are updates to the initial version for Tensorflow/Keras 2.3.1. The functions became deprecated since them, so here it is, updated for version 2.9.1.

手書き数字を認識するTensorflow/Kerasスクリプト（2本）です。`E_2_1.py`はMNISTの手書き数字データセットを用いてDNNを訓練するためのもので、`E_2_2.py`は生成された訓練データをもとに手書き数字を認識するユーザプログラムです。もともとは[実践OpenCV 4 for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html)の付録E.2「手書き数字推定モデル」に掲載したスクリプトです。出版時にはTensorflow 2.3.1対応でしたが、それからAPIに変更があったので改定しています。Tensorflow/Keras 2.9.1で動作確認をしています。


### Files

#### [E_2_1.py](./E_2_1.py)

Download the MNIST (Modified NIST) handwritten numbers dataset, construct Neural-Network model, and train the model using the dataset.

The dataset is downloaded from [NIST (National Institute of Standards and Technology)](https://www.nist.gov/srd/nist-special-database-19) and saved as `$HOME/.keras/mnist.npz`. The file is a numpy-zip file.

The code then constructs a sequential model, train the model using the NIST data, and writes the structure/weight files under the `mnist_model_v2` directory in current working directory.


#### [E_2_2.py](./E_2_2.py)

A handwritten number recognition script. Just draw strokes on the 300x300 window using your mouse (left-button press), then hit `Enter`. The predicted number is shown in the top-left region. The number and its probability are shown on the console (command prompt). Enter `ESC` to clear the window. `Q` to quit.

<img src="./images/sample.png" width=150></img>


#### Others

Personal exercise/test scripts.

- [nist_data.py](./nist_data.py): Test-reads the MNIST dataset file (numpy zip file) and parses it. It then randomly shows 10 images and its associated number on the window. The data is from the test (`x_test` and `y_test`). As it shows, the MNIST file contains 60,000 training data and 10,000 test data. The image size is 28x28 (e.g., the shape of x_test is `(10000, 28, 28)`).
- [test_model.py](./test_model.py): Test-runs the trained model. It randomly reads the test data and feeds it to the model. The `x_test` index number, expected answer from `y_test`, and the predicted number and its probability are shown on the console. The image is also shown on the window. Press ESC to quit. Use any other key to continue the test.
- [to_categorical.py](./to_categorical.py): Tests `tf.keras.utils.to_categorical`.


## References

- ["実践OpenCV 4 for Python 画像映像情報処理と機械学習"](https://www.cutt.co.jp/book/978-4-87783-460-9.html), 2021-01-20.
- [Training a neural network on MNIST with Keras](https://www.tensorflow.org/datasets/keras_example) (Tensorflow documentation). The author uses a Flatten → Dense(128) → Dense(10) model.
- [MNIST Dataset Prediction Using Keras!](https://www.analyticsvidhya.com/blog/2021/06/mnist-dataset-prediction-using-keras/), 2021-06-01. Dense(32) → Dense(64) → Dense(10) model.
- [MNIST Handwritten Number Recognition using Keras — with live predictor — with source code](https://towardsdev.com/mnist-handwritten-number-recognition-using-keras-with-live-predictor-with-source-code-2523c45ea950), 2022-01-07. Conv2D(32) → MaxPooling2D → Conv2D(64) → MaxPooling2D → Dropout(0.25) → Flatten → Dense(128) → Dropout(0.5) → Dense(10) model.
- [MNIST Handwritten Digit Recognition in Keras](https://nextjournal.com/gkoehler/digit-recognition-with-keras), 2020-02-18. Dense(512) → Activation('relu') → Dropout(0.2) → Dense(512) → Activation('relu') → Dropout(0.2) → Dense(10) → Activation('softmax')
