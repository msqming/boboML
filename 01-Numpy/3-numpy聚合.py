#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

# 聚合运算
L = np.arange(16).reshape(4,-1)
print(np.sum(L))
print(np.sum(L,axis=0)) # 0沿着列轴和向量  1沿着行轴的和向量
print(np.mean(L)) # 平均值
print(np.median(L)) # 中位数
print(np.percentile(L,q=50))  # 百分位数
print(np.var(L))  # 方差
print(np.std(L))  # 标准差


# 索引
X = np.random.normal(0,1,size=1000000)
print(np.argmin(X)) # 最小值的索引位置
print(np.min(X))
print(X[np.argmin(X)])

# 排序和使用索引
x = np.arange(16)
np.random.shuffle(x) # 乱序操作 [ 3  7  9  4 10  2 14 11 12  1 13  0 15  8  6  5]
print(np.argsort(x)) # 元素排序好的索引 [11  9  5  0  3 15 14  1 13  2  4  7  8 10  6 12] 0在上个数组的第11索引，1在第9索引，以此类推
print(x)
print(np.sort(x))  # 排序


# 矩阵排序
Z = np.random.randint(10,size=(4,4))
print(np.sort(Z,axis=1))  # 按行向量排序
print(np.sort(Z,axis=0))  # 按列向量排序

