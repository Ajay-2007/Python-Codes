# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 23:02:12 2019

@author: d33ps3curity
"""


import numpy as np

my_list = [1, 2, 3, 4, 5]
np.array(my_list)

# Creating a 3*4 zeros array
X = np.zeros((3, 4)) # default datatype float64
print(X)
print()

# Takes shapes as an argument
ones_array = np.ones((5, 4))
print("ones_array is \n", ones_array)

full_array = np.full((4, 3), 5)
print(full_array)


# creating identity matrix using eye function of numpy

identity_matrix = np.eye(5)
print(identity_matrix) # since identity matrix are square matrix it only takes
                        # one argument to specify the size of the matrix
print(identity_matrix.dtype)

# Creating diagonal matrix
diagonal_matrix = np.diag([10, 20, 30, 40, 50])
print(diagonal_matrix)
print(diagonal_matrix.dtype)

# Creating numpy arrays within a range

array_within_range = np.arange(10)
print(array_within_range)

# since the step number is not given it will start with 4 and stop
# till 10 - 1 cause stop number is exclusive
array_within_range_2 = np.arange(4, 10)
print(array_within_range_2)

# third argument is the distance between any two value in the
# created array
array_within_range_3 = np.arange(4, 15, 3)
print(array_within_range_3)

# Numpy linspace function for creating sequences of floating point
# number array
print()
# here start and endpoints both are inclusive
linspace_function = np.linspace(0, 25)
print(linspace_function)
print()
# here we can specify the step value that we want defaults to 50
linspace_function_2 = np.linspace(0, 25, 10)
print(linspace_function_2)
print()

# we can even specify that whether we want to include the endpiont or not
linspace_function_3 = np.linspace(0, 25, 10, endpoint=False)
print(linspace_function_3)
print()


# combining arange and linspace function to create Rank-2 array

rank_2_array = np.reshape(linspace_function_2, (5, 2))
print(rank_2_array)
print(np.reshape(linspace_function_2, (2, 5)))

# we can not reshape an array greater than its size
# error_rank_array = np.reshape(linspace_function_2, (5, 5))

# print(error_rank_array)

##########################################################
# Creating numpy array in one line using arange, linspace and reshape
# function

inline_array = np.arange(25).reshape(5, 5)
print(inline_array)

# using linspace the third argument in linspace is for how much element we
# want in our numpy array

inline_array_linspace = np.linspace(1, 25, 25, endpoint = False).reshape(5, 5)
print(inline_array_linspace)

# create numpy array that contains random numbers, often in machine learning
# you need to create random matrices for example when initializing the
# weight of a Neural Network
rand_no_array = np.random.random((3, 3))

print(rand_no_array)

# creating numpy array with the random numbers in a given interval
rand_no_interval = np.random.randint(3, 34, (5, 6))
print(rand_no_interval)

# creating numpy array contaning elements satisfy some statistical property
# like normal distribution, bionomical distribution, gaussian distribution etc.

statistics_array = np.random.normal(0, 0.1, (1000, 1000))
print(statistics_array)

# printing important statistics data from the statistics_array
print('mean: ', statistics_array.mean())
print('standard daviation', statistics_array.std())
print('max:', statistics_array.max())
print('min:', statistics_array.min())
print('# positive numbers in array:', (statistics_array > 0).sum())
print('# negative number in array:', (statistics_array < 0).sum())
print(statistics_array.dtype)

# y = np.linspace()










