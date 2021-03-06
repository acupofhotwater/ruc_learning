# !/usr/bin/env python
# -*- coding:utf-8 -*-

# classified data
from sklearn import datasets
digits = datasets.load_digits()
print("input shape", digits.data.shape)     #input shape
print("output shape", digits.target.shape)   #output shape

# feature_extraction

# train test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(digits.data,
                                        digits.target,
                                        test_size = 0.2,
                                        random_state = 33) # 
# model setting

# rfc
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(x_train, y_train)
rfc_ypred = rfc.predict(x_test)

# xgboost
from xgboost import XGBClassifier
xgc = XGBClassifier()
xgc.fit(x_train, y_train)
xgc_ypred = xgc.predict(x_test)

# svm 
from sklearn import svm
svmc = svm.SVC()
svmc.fit(x_train, y_train)
svmc_ypred = svmc.predict(x_test)


# evaluate
from sklearn.metrics import accuracy_score
rfc_accuracy = accuracy_score(y_test, rfc_ypred)
print ("rfc accuarcy: %.2f" %(rfc_accuracy*100.0))

xgc_accuracy = accuracy_score(y_test, xgc_ypred)
print ("xgc accuarcy: %.2f" %(xgc_accuracy*100.0))

svmc_accuracy = accuracy_score(y_test, xgc_ypred)
print ("xgc accuarcy: %.2f" %(svmc_accuracy*100.0))


