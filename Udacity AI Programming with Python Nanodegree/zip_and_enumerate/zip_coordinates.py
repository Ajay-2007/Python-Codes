x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
# for each_tuple in zip(labels, x_coord, y_coord, z_coord)
for each_tuple in zip(labels,x_coord, y_coord, z_coord):
    # str1 = ""
    #label, x, y, z = each_tuple
    # str1 = label + ": "+ str(x) + ", " + str(y) + ", " + str(z)
    points.append("{} : {}, {}, {}".format(*each_tuple))
                           

for point in points:
    print(point)

############################################################
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))# replace with your code
print(cast)

###########################################################
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# Transpose of a matrix
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = [c for c in zip(*data)]
data_transpose2 = tuple(zip(*data))
print(data_transpose)
print(data_transpose2)
# write your for loop here
for index, height in enumerate(heights):
    cast[index] = '{} {}'.format(cast[index], height)
    

print(cast)

