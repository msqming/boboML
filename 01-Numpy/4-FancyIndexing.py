#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

x = np.arange(16)
print(x)
ind = [3, 5, 8]  # 索引列表
print(x[ind])
ind1 = np.array([[0, 2],
                 [1, 3]])  # 二维索引

print(x[ind1])

print(x <= 3)
print(np.sum(x <= 3))  # 求向量x小于等于3的所有元素个数的和
print(np.sum((x > 3) & (x < 6)))  # 大于3并且小于6 多种条件
print(np.sum((x < 3) | (x > 10)))  # 小于3 或 大于 10
print(np.count_nonzero(x <= 3))  # 另外一种方式求
print(np.any(x == 0))  # 查看向量x是否有0的元素

X = np.arange(16).reshape(4, 4)
print(X)
print(X[X[:, 3] % 3 == 0, :])  # 获取X矩阵最后一列能被3整除的数据
