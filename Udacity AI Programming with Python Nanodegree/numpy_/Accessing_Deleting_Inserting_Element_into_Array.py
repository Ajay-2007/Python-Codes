# # -*- coding: utf-8 -*-
# """
# Created on Sun Jul 28 00:45:14 2019

# @author: d33ps3curity
# """
# # accessing and modifying data from rank-1 array
# import numpy as np
import numpy as np
# x = np.array([1, 2, 3, 4, 5])

# print(x)
# print(x[0])
# print(x[2:4])
# x[3] = 20
# print(x)

# ##############################################################################
# # accessing data in rank-3 array

# x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(x)
# # this is how we access and modify  elements in rank-2 numpy array
# print(x[0,0])
# print(x[0,2])
# x[0, 2] = 20
# print(x)
# print(x[0,2])
# print(x[0][2])


# ##############################################################################
# # How we can add and delete the elements from ndarrays
# x = np.array([1, 2, 3, 4, 5])
# y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print()
# print('Original x=',x)
# # delete the first and last element of x
# x = np.delete(x, [0, 4], axis=0)
# print()
# print('Modified x = ',x)

# print('Original y :', y)
# # delete the first row of y
# w = np.delete(y, 0, axis=0)
# print()
# print('Modified y:\n', w)

# print()
# # delete the first and last colum of y
# v = np.delete(y, [0, 2], axis=1)
# print('Modified y : \n{}'.format(v))


# ##############################################################################
# # How can we append values to ndarrays
# x = np.array([1, 2, 3, 4, 5])
# print(x)
# print()
# x = np.append(x, 6)
# print(x)
# print()
# x = np.append(x, [7, 8, 9])
# print(x)

# y = np.array([[1, 2, 3], [4, 5, 6]])
# print('Original y:\n',y )
# # appending a row to an ndarray y
# v = np.append(y, [[7, 8, 9]], axis = 0)
# print('Modified y\n', v)

# w = np.append(y, [[9], [10]], axis = 1)
# print('Modified y :\n', w)





##############################################################################
# How can we insert into ndarray
# using insert function
# np.insert(ndarray, index, values, axix)

x = np.array([1, 2, 5, 6, 7])
print(x)
x = np.insert(x, 2, [3, 4], axis=0)
print(x)

y = np.array([[1, 2, 3], [7, 8, 9]])

print(y)
print()
# inserting [4, 5, 6] into row of y between row one and two
v = np.insert(y, 1, [4, 5, 6], axis = 0)
print(v)

# inserting 5 into column
w = np.insert(y, 1, 5 , axis = 1)
print(w)



















