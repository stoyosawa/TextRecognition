## README

<a style="float: right;" href="./README.jp.md"><img src="https://www.worldometers.info/img/flags/ja-flag.gif" width="50">日本語版</a>

This repository contains text-recognition scripts. They are updates/revisions of the codes described in the following books:

- Nagata and Toyosawa: [実践OpenCV 4 for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html), Cutt System, Jan 2021.
- Nagata and Toyosawa: [実践OpenCV 3 for C++ 画像映像情報処理](https://www.cutt.co.jp/book/978-4-87783-380-0.html), Cutt System, Sep 2017.
- Kuwaim Toyosawa and Nagata: [実践OpenCV 2.4 for Pythonー映像処理&解析](https://www.cutt.co.jp/book/978-4-87783-346-6.html), Cutt System, Jul 2014.


### Table of contents

- [MNIST handwritten numbers recognition](./MnistHandWriting/README.md)
- [East text detector](./East/README.md)
- [Image tilt adjustment using Hough transformation](./Hough/README.md)


### Requirements

You need Python (naturally) and the following libraries.

```
pip install tensorflow                                   # Tensorflow/Keras.
pip install opencv-python                                # OpenCV for Python.
pip intall numpy                                         # It usually comes with OpenCV.
pip install pillow                                       # Used in MNIST.
pip instll imutils                                       # Used in EAST.
```