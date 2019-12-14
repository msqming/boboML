#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

X = np.arange(1,16).reshape(3,5)
# 在进行多维矩阵运算时，矩阵里面的每一个元素都会进行运算
X1 = X + 1  # + - * / 等等其它数学运算
print(X1)
# 多维矩阵与多维矩阵的运算
A = np.arange(4).reshape(2,2)
B = np.full((2,2),10)
C1 = A + B  # 对应元素做相应的操作，+ - * / 等等其它数学运算
print(C1)
# 标准的矩阵乘法
C2 = A.dot(B)
print(C2)

# 矩阵的转置 行变列，列变行
D = np.arange(4).reshape(2,2)
print(D)
print(D.T)

# 矩阵的逆
E = np.arange(4).reshape(2,2)
E1 = np.linalg.inv(E) # 矩阵E的逆
print(E1)
# 伪逆矩阵
F = np.arange(16).reshape(2,8)
print(F)
pinvF = np.linalg.pinv(F)
print(pinvF)
F1 = F.dot(pinvF)
print(F1)