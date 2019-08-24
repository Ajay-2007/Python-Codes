# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:44:59 2019

@author: d33ps3curity
"""

import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5.5, 6.5, 7.5, 8.5])

print('Performing basic element-wise operatios using arithmetic symbols and\
      functions')

# Both forms will do the same operation, the only difference is that is you
# use the function approach, the functions usually have options that you can
# tweak using keywords.
print('x + y = ', x + y)
print('add(x, y)', np.add(x, y))
print('x - y', x - y)
print('subtract(x, y)', np.subtract(x, y))
print('x * y', x * y)
print('multiply(x, y)', np.multiply(x, y))
print('x / y', x / y)
print('divide(x, y)', np.divide(x, y))

# performing the same operation in rank-2 ndarray
X = np.array([1, 2, 3, 4]).reshape(2, 2)
Y = np.array([5.5, 6.5, 7.5, 8.5]).reshape(2, 2)

print('Performing basic element-wise operations using arithmetic symbols\
      and functions')

print('X + Y', X + Y)
print('X - Y', X - Y)
print('X * Y', X * Y)
print('X / Y', X / Y)

print('add(X, Y)', np.add(X , Y))
print('subtract(X , Y)', np.subtract(X, Y))
print('multiply(X, Y)', np.multiply(X, Y))
print('divide(X, Y)', np.subtract(X, Y))

# We can also apply mathematics functions, such as sqrt(x), to all elememts of
# ndarray at once
# applying different mathematics functions to all element of x
x = np.array([1, 2, 3, 4])
print('EXP(x)', np.exp(x))
print('SQRT(x)', np.sqrt(x))
print('POW(x, 2)', np.power(x, 2))



# Numpy has variety of statistical functions. Statistical functions provide
# us with statistical information about the elements in an ndarray.

X = np.array([[1, 2], [3, 4]])

print('Average of all elements in X', np.mean(X))
print('Average of all elements in the columns of X', np.mean(X, axis = 0))
print('Average of all elements in the rows of X', np.mean(X, axis = 1))
print()
print('Sum of all elements in X:', np.sum(X))
print('Sum of all elements in the columns of X', np.sum(X, axis = 0))
print('Sum of all elements in the rows of X', np.sum(X, axis = 1))
print()
print('Standard Deviation of all elements in X:',np.std(X))
print('Standard Deviation of all elements in columns of X', np.std(X, axis = 0))
print('Standard deviation of all elements in rows of X', np.std(X, axis = 1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in columns of X', np.median(X, axis = 0))
print('Median of all elements in rows of X', np.median(X, axis = 1))
print()
print('Maximum value of all elements in X', np.max(X))
print('Maximum value of all elements in columns of X', np.max(X, axis = 0))
print('Maximum value of all the elements in rows of X', np.max(X, axis = 1))
print()
print('Minimum value of all the elements in X', np.min(X))
print('Minimum value of all the elements in columns of X', np.min(X, axis = 0))
print('Minimum value of all the elements in rows of X', np.min(X, axis = 1))

###############################################################################
# Numpy can addi single numbers to all the elements of an ndarray without the use
# of complicated loops

X = np.array([[1, 2], [3, 4]])
print('3 * X = \n', 3 * X)
print()
print('3 + X = \n', 3 + X)
print()
print('3 - X = \n', 3 - X)
print()
print('3 /  X = \n', 3 / X)

# In the examples above numpy is working behind the scenes to broadcast
# 3 along the ndarray so that they have the same shape. This allows us to
# add 3 to each element of X with just one line of code

# Subject to constraints, Numpy can do the same for two ndarrays of different
# shapes

x = np.array([1, 2, 3])
Y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
Z = np.array([1, 2, 3]).reshape(3, 1)
print(x)
print()
print(Y)
print(X)
print('x + Y\n', x + Y)
print('Z + Y\n', Z + Y)
# numpy is able to add 1 x 3 and 3 x 1 ndarrays to 3 x 3 ndarrays by
# broadcasting the smaller ndarrays along the big ndarray so that they have
# compatible shapes.

# Numpy can do this provided that the smaller ndarray,  such as the 1 x 3
# ndarray in our example, can be expanded to the shape of the larger ndarray in
# such a way that the resulting boradcast is unambigous
















