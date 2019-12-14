#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import datasets

digits = datasets.load_digits()
X = digits.data
y = digits.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=66)

def f1():
    param_grid = [
        {
            'weights': ['uniform'],
            'n_neighbors': [i for i in range(1, 11)]
        },
        {
            'weights': ['distance'],
            'n_neighbors': [i for i in range(1, 11)],
            'p': [i for i in range(1, 6)]
        }
    ]
    # 通过网格搜索得到最优的超参数
    knn_clf = KNeighborsClassifier()
    grid_search = GridSearchCV(knn_clf, param_grid, n_jobs=-1)  # verbose参数显示信息
    grid_search.fit(X_train, y_train)

    # print(grid_search.best_estimator_)
    print(grid_search.best_score_)
    # print(grid_search.best_params_)

    # 把最优的超参数赋值给KNN算法
    knn_clf = grid_search.best_estimator_

    score = knn_clf.score(X_test, y_test)
    print(score)


from timeit import timeit

t = timeit('f1()', 'from __main__ import f1', number=1)
print(t)
# 0.9860821155184412
# 0.9916666666666667

# 1核
# 25.02595047

# 4核运行
# 13.77001563

# 8核运行
# 6.694541411
