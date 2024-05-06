# CHALLENGE 02: Find pairs

# Pairs / Two Sum - LeetCode 1

numbers = [2, 6, 3, 9, 11]


def find_pairs(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                continue
            elif arr[i] + arr[j] == target:
                print(i, j)


find_pairs(numbers, 9)
