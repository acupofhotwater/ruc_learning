# !/usr/bin/env python
# -*- coding:utf-8 -*-

# classified data
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.data.shape)
# regression data
from sklearn.datasets import load_boston
boston = load_boston()
print (boston.data.shape)
# train test
