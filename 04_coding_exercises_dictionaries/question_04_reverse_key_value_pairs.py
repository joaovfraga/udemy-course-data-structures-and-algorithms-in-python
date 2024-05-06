# Question 04 - Reverse Key-Value Pairs

# How I did it:
def reverse_dict(my_dict):
    new_dict = {value:key for (key, value) in my_dict.items()}
    return new_dict


my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))

# How the professor did it:
def reverse_dict2(my_dict2):
    return {v: k for k, v in my_dict2.items()}


my_dict2 = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict2(my_dict2))