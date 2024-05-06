from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])

# Percorrendo um 01_array
def traverseArray(array):
    for i in array:
        print(i)

# traverseArray(arr1)

# Acessando elementos no 01_array
def accessElement(array, index):
    if index >= len(array):
        print("There is not any element in this index")
    else:
        print(array[index])
# accessElement(arr1, 6)

# Finding an element
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

# print(linear_search(arr1, 10))

# Deleting an element from the 01_array

arr1.remove(1)
print(arr1)