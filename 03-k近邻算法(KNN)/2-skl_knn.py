#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

X = iris.data
y = iris.target

# 分割训练数据集与测试数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)  # 默认0.2

knn_clf = KNeighborsClassifier(n_neighbors=5)  # 传入K值
knn_clf.fit(X_train, y_train)  # 模型拟合

y_predict = knn_clf.predict(X_test)  # 返回测试数据集的结果

# 检验预测准确率
accuracy = accuracy_score(y_test,y_predict)
score = knn_clf.score(X_test,y_test)
print(accuracy,score)

