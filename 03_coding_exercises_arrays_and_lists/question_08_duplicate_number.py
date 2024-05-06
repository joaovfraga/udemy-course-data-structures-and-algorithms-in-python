# QUESTION 08 - Duplicate Number
# Write a function to remove the duplicate numbers on given integer array/list.

# My Solution:
def remove_duplicates(arr):
    new_list = []

    for i in arr:
        if i in new_list:
            continue
        else:
            new_list.append(i)

    return new_list


print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))


# Professor Solution:
def remove_duplicates(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst


my_list = [1, 1, 2, 2, 3, 4, 5]
print(remove_duplicates(my_list))
