# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 00:18:19 2019

@author: d33ps3curity
"""


import numpy as np

# Using the Built-in functions you learned about in the
# previous lesson, create a 4 x 4 ndarray that only
# contains consecutive even numbers from 2 to 32 (inclusive)

X = np.arange(2, 34, 2)
print(X)
print(X.reshape(4, 4))
array = np.linspace(2, 32, 16, endpoint = True).reshape((4, 4))
print(array)
print()
Y = np.linspace(2, 32, 16).reshape(4, 4)
print(Y)








