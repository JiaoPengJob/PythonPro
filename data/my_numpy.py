#!/usr/bin/env python
# -*- coding : utf-8 -*-

# Numpy

import numpy as np

"""
numpy.array(object, dtype = None, copy = True, order = None, subok = False, ndmin = 0)
object:任何暴露数组接方法的对象都会返回一个数组或任何序列
dtype:数组的所需数据类型
copy:默认为true，对象是否被复制
order:C，按行；F按列；A，任意，默认
subox:默认情况下，返回的数组被强制为基数数组，如果为True，则返回子类
ndimin:
"""
nas = np.array([[1, 2, ], [3, 4]], dtype=str)
# print(nas)
"""
numpy.dtype(object, align, copy)
object：被转换为数据类型的对象
align：如果为True，则向字段添加间隔，使其类似于C的结构体
copy：是否生成dtype对象的新副本
"""

"""
numpy.empty(shape, dtype = float, order = 'C')
shape:空数组的形状
dtype:所需的输出数组类型
order:“C”按行，“F”按列
"""

"""
numpy.zeros(shape, dtype = float, order = 'C')
shape:空数组的形状，整数或整数元组
dtype:输出类型
order:“C”按行，“F”按列
"""

"""
numpy.frombuffer(buffer, dtype = float, count = -1, offset = 0)
buffer:任何暴露缓冲区接口的对象
dtype:输出类型
count:需要读取的数据数量，默认为-1，读取所有数据
offset:需要读取的起始位置，默认为0
"""

"""
numpy.arange(start, stop, step, dtype)
start：范围的起始值，默认0
stop：范围的终止值
step：两个值的间隔，默认1
dtype：输出类型
"""

"""
numpy.linspace(start, stop, num, endpoint, retstep, dtype)
start：序列的起始值
stop：序列的终止值，如果endpoint为True，该值包含在序列中
num：要生成的等间隔样例数量，默认为50
endpoint：序列中是否包含stop值
retstep：True，返回样例，以及连续数字之间的步长
dtype：输出的数据类型
"""

"""
numpy.logscale(start, stop, num, endpoint, base, dtype)
start：起始值是base ** start
stop：终止值是base ** stop
num：范围内的数值数量，默认为50
endpoint：True，终止值包含在输出数组中
base:对数空间的底数，默认为10
dtype:输出的数据类型
"""

"""
numpy.reshape(arr, newshape, order')
arr：原数组
newshape：整数或整数数组，新的形状兼容原有形状
order：顺序，C，F，A
"""

arr = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
arrs = np.array([11, 22, 33, 44, 55, 66])

print(arr + arrs)
