# Question 05 - Conditional Filter

# How I did it:
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)