# QUESTION 10 - Contains Duplicate
#   Given an integer array nums, return true if any value appears at least twice in the array,
#   and return false if every element is distinct.

# My Solution
def contains_duplicate(numbers):
    new_list = []
    for num in numbers:
        if num not in new_list:
            new_list.append(num)

    if numbers != new_list:
        return True
    else:
        return False


nums = [1, 2, 3, 1]
print(contains_duplicate(nums))


# Professor Solution:
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Example usage
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
print(contains_duplicates(nums))
