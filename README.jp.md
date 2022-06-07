## README

このリポジトリには、次に示す書籍で紹介した文字認識関連のスクリプトの改定版を収容しています。

- 永田 & 豊沢: [実践OpenCV 4 for Python 画像映像情報処理と機械学習](https://www.cutt.co.jp/book/978-4-87783-460-9.html), カットシステム（2021年1月）.
- 永田 & 豊沢: [実践OpenCV 3 for C++ 画像映像情報処理](https://www.cutt.co.jp/book/978-4-87783-380-0.html), カットシステム（2017年9月）.
- 桑井, 豊沢 & 永田: [実践OpenCV 2.4 for Pythonー映像処理&解析](https://www.cutt.co.jp/book/978-4-87783-346-6.html), カットシステム（2014年7月）.

ご購入はこちらから。

<table border=0>
 <tr>
  <td><img src="https://www.cutt.co.jp/book/images/978-4-87783-460-9.png" height="200"></img></td>
  <td><img src="https://www.cutt.co.jp/book/images/978-4-87783-380-0.png" height="200"></img></td>
  <td><img src="https://www.cutt.co.jp/book/images/978-4-87783-346-6.png" height="200"></img></td>
 </tr>
 <tr>
  <td><a href="https://honto.jp/netstore/pd-book_30749005.html">Honto</a> | <a href="https://www.amazon.co.jp/dp/4877834605">Amazon</a> | <a href="https://www.yodobashi.com/product/100000009003381130/">ヨドバシカメラ</a></td>
  <td><a href="https://honto.jp/netstore/pd-book_28612900.html">Honto</a> | <a href="https://www.amazon.co.jp/dp/4877833803">Amazon</a> | <a href="https://www.kinokuniya.co.jp/f/dsg-01-9784877833800">紀伊国屋</a></td>
  <td>古いのでOpenCV 4のほうをどうぞ</td>
 </tr>
</table>


#### 目次

- [MNIST手書き数字認識](./MnistHandWriting/README.jp.md)
- [EASTによる文字ローカライゼーション](./East/README.jp.md)
- [ハフ変換による傾き補正](./Hough/README.jp.md)


### 要求条件

スクリプトを走らせるにはPython（当然）と上記のライブラリが必要です。

```
pip install tensorflow                              # Tensorflow/Keras.
pip install opencv-python                           # OpenCV for Python.
pip install pillow                                  # Used in MNIST.
pip instll imutils                                  # Used in EAST.
```

他にNumpyが必要ですが、これはOpenCVを導入すれば自動的にインストールされます。
