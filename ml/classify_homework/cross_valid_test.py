# !/usr/bin/env python
# -*- coding:utf-8 -*-

# classify data
from sklearn import datasets
digits = datasets.load_digits()
print("input shape", digits.data.shape)     #input shape
print("output shape", digits.target.shape)   #output shape

# feature_extraction

# train valid test
from sklearn.model_selection import train_test_split
Xtrain, x_test, Ytrain, y_test = train_test_split(digits.data,
                                        digits.target,
                                        test_size = 0.2,
                                        random_state = 33) # 

'''from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score, make_scorer

best_score = 0
SVM_scores = []
for kernel in ['rbf', 'poly', 'linear']:
    for gamma in [0.0001, 0.001, 0.01, 0.1, 1.0]:
        for C in [0.001, 0.01, 0.1, 1, 10.0, 100]:
            svm = SVC(kernel= kernel, gamma=gamma, C=C)
            scores = cross_val_score(svm, Xtrain, Ytrain, cv=5, scoring='f1_micro')
            score = scores.mean()
            SVM_scores.append(scores.mean())
            if score > best_score:   
                best_score = score
                best_parameters = {'kernel': kernel, 'C': C, 'gamma': gamma}

print ("SVM_scores", SVM_scores)
print ("cross valid best_score", best_score)
print ("best_parameters", best_parameters)

svm = SVC(**best_parameters)
svm.fit(Xtrain, Ytrain)
y_predict_test = svm.predict(x_test)
test_socre = f1_score(y_test,y_predict_test, average='micro')
print("SVM test_socre", test_socre)'''


## RF classifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score, make_scorer


best_score = 0
RF_scores = []
for n_estimators in range(10,211,20):
    for max_depth in range(10,100, 10):
        for min_samples_split in range(100,201,10):
            rfc = RandomForestClassifier()
            scores = cross_val_score(rfc, Xtrain, Ytrain, cv=5, scoring='f1_micro')
            score = scores.mean()
            RF_scores.append(scores.mean())
            if score > best_score:   
                best_score = score
                best_parameters = {'n_estimators': n_estimators, 'max_depth': max_depth, 'min_samples_split': min_samples_split}

print ("RF_scores", RF_scores)
print ("cross valid best_score", best_score)
print ("best_parameters", best_parameters)


rfc = RandomForestClassifier(**best_parameters)
rfc.fit(Xtrain, Ytrain)
rfc_ypred = rfc.predict(x_test)
test_socre = f1_score(y_test,rfc_ypred, average='micro')
print("RF test_socre", test_socre)


'''# xgboost
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score, make_scorer
import numpy as np

max_depth_range = range(3,10,1)

best_score = 0
XG_scores = []

for max_depth in max_depth_range:
        xgc = XGBClassifier(max_depth=max_depth)
        scores = cross_val_score(xgc, Xtrain, Ytrain, cv=5, scoring='f1_micro')
        score = scores.mean()
        XG_scores.append(scores.mean())
        if score > best_score:   
            best_score = score
            best_parameters = {'max_depth': max_depth}

print ("XG_scores", XG_scores)
print ("cross valid best_score", best_score)
print ("best_parameters", best_parameters)

xgc = XGBClassifier(**best_parameters)
xgc.fit(Xtrain, Ytrain)
xgc_ypred = xgc.predict(x_test)
test_socre = f1_score(y_test,xgc_ypred, average='micro')
print("XGC test_socre", test_socre)'''