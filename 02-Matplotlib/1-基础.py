#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)
siny = np.sin(x)
cosy = np.cos(x)
# 折线图
plt.plot(x,siny,label='sin(x)')  # 折线图
plt.plot(x,cosy,color='r',linestyle='--',label='cos(x)')

plt.xlabel('x axis')
plt.ylabel('y value')
plt.legend() # 加上图示
plt.title('Welcome to the ML world!')

plt.show()

# 散点图
x1 = np.random.normal(0,1,10000)
y1 = np.random.normal(0,1,10000)
plt.scatter(x1,y1,alpha=0.2) # 透明度
plt.show()
