# !/usr/bin/env python
# -*- coding:utf-8 -*-

from sklearn.datasets import load_iris()
import pandas as pd
# get data
iris = load_iris()
df = pd.DataFrame(iris.data, co)
# train test