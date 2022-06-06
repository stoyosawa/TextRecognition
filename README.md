## README

This repository contains text-recognition scripts. They are updates/revisions of the codes described in the following books:

- Nagata and Toyosawa: [実践OpenCV 4 for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html), Cutt System, Jan 2021.
- Nagata and Toyosawa: [実践OpenCV 3 for C++ 画像映像情報処理](https://www.cutt.co.jp/book/978-4-87783-380-0.html), Cutt System, Sep 2017.

このリポジトリには、上記2冊の書籍で紹介した文字認識関連のスクリプトの改定版が収容されています。

### Table of contents

- [MNIST handwritten numbers recognition / MNIST手書き数字認識](./MnistHandWriting/README.md)
- [East text detector / EASTによる文字ローカライゼーション](./East/README.md)
- [Image tilt adjustment using Hough transformation/ ハフ変換による傾き補正](./Hough/README.md)


### Requirements

You need Python (naturally) and the following libraries.

```
pip install tensorflow                                   # Tensorflow/Keras.
pip install opencv-python                                # OpenCV for Python.
pip intall numpy                                         # It usually comes with OpenCV. Run this if it has been lost.
pip install pillow                                       # Used in MNIST.
pip instll imutils                                       # Used in EAST.
```

スクリプトを走らせるにはPython（当然）と上記のライブラリが必要です。


### ご購入はこちらから

<img src="https://www.cutt.co.jp/book/images/978-4-87783-460-9.png" height=200></img>
【
[Honto](https://honto.jp/netstore/pd-book_30749005.html) |
[Amazon.co.jp](https://www.amazon.co.jp/dp/4877834605) |
[ヨドバシカメラ](https://www.yodobashi.com/product/100000009003381130/)
】

<img src="https://www.cutt.co.jp/book/images/978-4-87783-380-0.png" height=200><img>
ご購入はこちらから【
[Honto](https://honto.jp/netstore/pd-book_28612900.html) |
[Amazon.co.jp](https://www.amazon.co.jp/dp/4877833803) |
[紀伊国屋](https://www.kinokuniya.co.jp/f/dsg-01-9784877833800/)
】


### History

- 2017-05-29: `7_6.cpp` for character localization using Nuemann & Mates alogorithm (C++ & OpenCV 3.2 Contrib) was originally written for "OpenCV 3 for C++".
- 2017-09-10: "OpenCV 3 for C++" published.
- 2020-09-29: `E_2_1.py` and `E_2_2.py` for MNIST handwritten numbers recognition was originally written for "OpenCV 4 for Python".
- 2021-01-20: "OpenCV 4 for Python" published.
- 2022-05-27: MNIST scripts Updated for Tensorflow 2.9.1.
- 2022-06-06: Character localization script rewritten using EAST.

