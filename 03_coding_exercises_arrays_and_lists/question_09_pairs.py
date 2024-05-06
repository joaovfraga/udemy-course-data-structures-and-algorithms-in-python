# QUESTION 09 - Pairs
#   Write a function to find all pairs of an integer array whose sum is equal to a given number. Do
#   not consider commutative pairs.

def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result


lista = [2, 4, 3, 5, 6, -2, 4, 7, 8, 9]
target = 7
print(pair_sum(lista, target))