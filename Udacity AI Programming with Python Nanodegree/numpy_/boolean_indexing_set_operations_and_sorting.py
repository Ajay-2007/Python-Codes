# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 12:27:47 2019

@author: d33ps3curity
"""


# Boolean indexing can help us to select elements using logical arguments
# instead of explicit indices

import numpy as np

X = np.arange(25).reshape(5, 5)
print(X)
print('THe elements in X that are greater than 10 are:')
print(X[X > 10])

print()
print('The elements in X that are less than 17 are:')
print(X[X < 17])

print()
print('The elements in X that are between 10 and 17 are :')
print(X[(X > 10) & (X < 17)])

# Use Boolean indexing to assign the elements that are between 10 and 17 the
# value of -1
X[(X > 10) & (X < 17)] = -1
print(X)

###############################################################################
x = np.array([1, 2, 3, 4, 5])
y = np.array([6, 7, 2, 8, 4])

print('The elements that are both in x and y:', np.intersect1d(x, y))
print('The elements that are in x but not in y:', np.setdiff1d(x, y))
print('All the elements of x and y:', np.union1d(x, y))

###############################################################################
x = np.random.randint(1, 11, size=(10,))
print('sort x and print the sorted array using sort as a function')
print(np.sort(x))

# When we sort out of place the original array remains intact.
print('x after sorting:', x)

# we can sort only the unique value of x by combining the sort function with
# the unique function.
print(np.sort(np.unique(x)))

# How we can sort ndarrays in place, by using sort as a method

# sort x and print the sorted array using sort as a method
print('x before sorting using sort as a method')
print(x)
x.sort()

# When we sort in place the original array is changed to the sorted array.
print('x after sorting:', x)
print(np.unique(x))

###############################################################################
# When sorting rank 2 ndarrays, we need to specify to np.sort() function
# whether we are sorting by rows or columns. This is done by using the axis
# keyword

x = np.linspace(1, 10, 25).reshape(5,5)
x  = np.arange(1, 26).reshape(5,5)
x = np.random.randint(1, 11, size=(5, 5))
print(x)
print('We sort the columns of x and print the sorted array')
print(np.sort(x, axis = 0))

print('sort the rows of x and print the sorted array')
print(np.sort(x, axis = 1))




