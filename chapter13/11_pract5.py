from functools import reduce
max2 = lambda a, b : max(a, b)

list = [1, 2, 13, 4, 8]

max1 = reduce(max2, list)
# a = reduce(max, list)
# print(a)
print(max1)