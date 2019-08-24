# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 10:15:07 2019

@author: d33ps3curity
"""


import numpy as np

x = np.arange(1, 21).reshape(4, 5)
print(x)

# Select all the elements that are in the 2nd through 4th rows and in the
# 3rd to 5th columns
print()
z = x[1:4, 2:5]
print(z)

# We can select the same element as above using method 2
print()
y = x[1:, 2:]
print(y)

print()
a = x[:3, 2:]
print(a)
# Select all the elements that are in the 1st through 3rd rows and in the 3rd
# to 4th columns
print()
v = x[:3, 2:4]
print(v)
print()
# Select all the elements in the 3rd row
print(x[2, :])
print()
# Select all the elements in the 3rd column
print(x[:, 2])
print()

# Select all the elements in the 3rd column and return it as a rank-2 array
print(x[:,2:3])
print()
# Its important to know that, when we perform slices on numpy arrays
# and save them into new variables the data is not actually copied into the
# new variable
X = np.arange(20).reshape(4, 5)
print()
print(X)
# Select all the elements that are in the 2nd through 4th rows and in the 3rd
# to 5th columns
Z = X[1:4, 2:5]
print()
print(Z)
Z[2,2] = 555
# Changes in Z have effect on X (the original ndarray) as well
print(X)
print()
print(Z)

###############################################################################
# If we want to create a new ndarray that contains a copy of the values in the
# slice, we need to use the np.copy() function

X = np.arange(20).reshape(4, 5)
print(X)
print()
# create a copy of the slice using the np.copy() function
Z = np.copy(X[1:4, 2:5])
Z[2, 2] = 555
print(X)
# It doesn't affect X (the origincal array now)
print(Z)
print()
# Create a copy of the slice using the copy as a method
# We can clearly see that by using the copy command, we are creating new
# ndarrays that are completely independent of each other

W = X[1:4, 2:5].copy()
print(X)
W[2, 2] = 444
print(W)


###############################################################################
# It is often useful to use one ndarray to make slices, or change elements in
# another ndarray.

indices = np.array([1, 3])
X = np.arange(20).reshape(4,5)

# use the indices ndarray to select the 2nd and 4th row of X
print()
Z = X[indices, :]
print(Z)

# use the indices ndarray to select 2nd and 4th column of X
print()
W = X[:, indices]
print(W)

###############################################################################
# Numpy also offers built-in function to select specific elements within
# ndarrays
# np.diag(ndarray, k=N) function extrats the elements along the diagonal
# defined by N. As default is k = 0 which refers to the main diagonal
# k > 0 are used to select elements in diagonal above the main diagonal
# k < 0 are used to select elements in diagonals below the main diagonal

X = np.arange(20).reshape(4, 5)

# elements in the main diagonal of X
print(X)
print('elements in the main diagonal of X\n')
print(np.diag(X))
# elements above the main diagonal
print()
print('elements above the main diagonal')
print(np.diag(X, k = 1))
# elements below the main diagonal
print('elements below the main diagonal')
print(np.diag(X, k = -1))
# elements above the main diagonal k = 2
print('elements above the main diagonal k = 2')
print(np.diag(X, k = 2))

###############################################################################
X = np.array([[1, 2, 3], [5, 2, 8], [1, 2, 3]])
# printing the unique elements of X
print('The unique elements in X are : ')
print(np.unique(X))
















