# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
test classifier 
'''
from sklearn import datasets

# get data
iris = datasets.load_iris()

x = iris.data
y = iris.target
# train test valid

# classify method
# linear regression
from sklearn import linear_model
linear = linear_model.LinearRegression()
linear.fit(x,y)
print("linear's score: ", linear.score(x,y))
linear.coef_ 
linear.intercept_ 
print("predict: ", linear.predict([7, 5, 2, 0.5], [7.5, 4 , 7, 2]))

# logistic regression
from sklearn import linear_model
logistic = linear_model.LogisticRegression()
logistic.fit(x, y)

# decision tree
from sklearn import tree
d_tree = tree.DecisionTreeClassifier(criterion='entropy')
    #Gini、Information Gain、Chi-square、entropy
d_tree.fit(x, y)

# svm
from sklearn import svm
svm_classifier = svm.SVC()

# naive bayes
from sklearn import naive_bayes
n_bayes = naive_bayes.GaussianNB()

# knn 
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=3)
knn.fit(x, y)





