# QUESTION 11 - Permutation
#  Given 2 lists return True if they are permutation of each other or False if they're not.
# What's Permutation? If two strings are Permutation, they have the same characters but in different orders.


def permutation(list1, list2):
    if len(list1) != len(list2):
        return False

    list1.sort()
    list2.sort()
    if list1 == list2:
        return True
    else:
        return False


list_1 = ["j", "o", "a", "o"]
list_2 = ["a", "o", "o", "j"]

print(permutation(list_1, list_2))