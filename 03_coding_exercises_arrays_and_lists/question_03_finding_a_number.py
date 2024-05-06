# QUESTION 03 - Finding a number in a Array.
#  Here we are going to implement Linear Search.

import numpy as np

myArray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])


def linear_search(arr, num):
    for i in range(len(arr)):
        if arr[i] == num:
            print(f"The number {num} exists in the Array")
            return

    print("This number does not exist in the Array")


linear_search(myArray, 0)
