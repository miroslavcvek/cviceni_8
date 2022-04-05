import numpy as np

# my_array = np.array([0, 1, 2, 3]
# print(my_array)
#
# my_array = np.zeros(4)
# print(my_array)
# my_array = np.ones(4)
# print(my_array)
#
# my_array = np.random.rand(4)
# print(my_array)
#
# my_array = np.arange(1, 6, 2)
# print(my_array)
#
# my_array = np.array([0, 1, 2, 3])
# print(my_array[2])
#
# for number in my_array:
#     print(number)

my_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(my_array)
print(my_array[0, 1:3])

my_array = np.random.rand(2, 3, 2)
print(my_array)
print(my_array[0, 1, 0])

# Vyzkoušej a analyzuj výstup
my_array = np.array([0, 1, 2, 3])
my_multiplied_array = my_array * 5
print(my_multiplied_array)
my_binary_array = my_array > 1
print(my_binary_array)

my_array1 = np.array([0, 1, 2, 3])
my_array2 = np.array([1, 1, 2, 2])
print(my_array1 + my_array2)

my_array = np.array([2, 3, 4, 5, 6, 7])
my_array_index = np.array([0, 2, 4])
print(my_array[my_array_index])

my_array = np.array([2, 3, 4, 5, 6, 7])
my_array_index = np.array([0, 2, 4])
print(my_array[my_array_index])

my_array = np.array([0, 1, 2, 3])
values = my_array[my_array > 1]
print(values)
my_array[my_array > 1] = 99
print(my_array)

my_array_float = np.ones(4, dtype=float)
print(my_array_float.dtype)
my_array_int = my_array.astype(int)
print(my_array_int.dtype)

my_array = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
array_shape = my_array.shape
print(array_shape)
my_array = my_array.reshape([4, 2])
print(my_array)
array_shape = my_array.shape
print(array_shape)

# np.sum() soucet np.mean() stred np.sqrt() odmocnina np.round() np.max() maximum np.argmax() misto maxima np.sort() rozdělit np.unique() unikat

pole_s_hodnotami = np.arange(1, 20, 1)
print(pole_s_hodnotami)

umocneni = pole_s_hodnotami * 3
print(umocneni)

pole_s_hodnotami[pole_s_hodnotami > 10] = 0
print(pole_s_hodnotami)

soucet = np.sum(pole_s_hodnotami)
print(soucet)

max = np.max(soucet)
print(max)