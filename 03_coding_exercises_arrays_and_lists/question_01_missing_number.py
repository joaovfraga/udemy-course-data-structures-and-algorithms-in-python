# Finding a missing number

myList = [1, 2, 3, 4, 6, 7, 8, 9, 10]


def find_missing_number(arr, n):
    sum1 = n * (n + 1) / 2
    sum2 = sum(arr)
    print(sum1 - sum2)


find_missing_number(myList, 10)
