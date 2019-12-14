#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

nparr = np.array([i for i in range(10)])
print(nparr)  # [0 1 2 3 4 5 6 7 8 9]

# 赋值
nparr[3] = 3.14
print(nparr)  # [0 1 2 3 4 5 6 7 8 9] 数据类型不会更改，还是int类型

nparr2 = nparr.astype('float64')  # 强制转换数据类型
print(nparr2)
print(nparr2.dtype)

nparr3 = np.arange(0,20,0.5)
print(nparr3)

nparr4 = np.linspace(0,20,11)
print(nparr4)

# 随机数
nparr5 = np.random.randint(0,10,size=10)  # 向量
print(nparr5)
nparr6 = np.random.randint(2,10,size=(3,5))  # 矩阵
print(nparr6)

# 随机种子
np.random.seed(66) # 随机种子
nparr7 = np.random.randint(2,10,size=(3,4))
np.random.seed(66)
nparr8 = np.random.randint(2,10,size=(3,4))
print(nparr7)
print(nparr8)

# 0~1之间的均匀分布随机矩阵
nparr9 = np.random.random(size=(3,4))
print(nparr9)

# 0~1之间的正态分布随机矩阵(均值为0，方差为1)
nparr10 = np.random.normal(size=(3,4))
print(nparr10)
nparr11 = np.random.normal(10,100)  # 均值为10，方差为100 的随机数

# # 0~1之间的正态分布随机矩阵(均值为0，方差为1)
nparr12 = np.random.normal(0,1,size=(3,4))
print(nparr12)

x = np.arange(10)
X = np.arange(15).reshape(3,5)
# 矩阵的访问
print(X,X[2,2])
print(X[:2,:3]) # 多维数组的切片
print(X[0,:])  # 取第一行
print(X[:,0])  # 取第一列

# 修改子矩阵会影响源矩阵,反之亦然
subX = X[:2,:3]
subX[0,0] = 100
print(X)
# 修改子矩阵不影响的操作
subX = X[:2,:3].copy()

# 将一维向量修改为多维矩阵
B = x.reshape(1,10)
print(x.shape)
print(B.shape)

# 只要两行的多维矩阵
C = x.reshape(2,-1)
# 只要5列的多维矩阵
D = x.reshape(-1,5)

# 一维向量合并操作
x1 = np.array([1,2,3])
y1 = np.array([3,2,1])
z1 = np.concatenate([x1,y1])  # [1 2 3 3 2 1]
print(z1)
# 多维矩阵合并操作(行向量增加)
A = np.arange(1,7).reshape(2,3)
print(A)
A1 = np.concatenate([A,A],axis=0)
print(A1)
# 多维矩阵合并操作(列向量增加)
A2 = np.concatenate([A,A],axis=1)
print(A2)
# 将一维向量合并到多维矩阵
A3 = np.concatenate([A,y1.reshape(1,3)],axis=0)
print(A3)
A4 = np.vstack([A,y1])  # 垂直方向堆叠
print(A4)
A5 = np.hstack([A,A2])  # 水平方向堆叠
print(A5)

# 多维矩阵分割
G = np.arange(16).reshape(4,4)
# G1,G2 = np.split(G,[2])
# print(G1,G2)

G3,G4 = np.vsplit(G,[2]) # 垂直方向分割 以第2行为分割点
G5,G6 = np.hsplit(G,[2]) # 水平方向分割 以第2列为分割点
print(G3,'====',G4)
print(G5,'====',G6)

