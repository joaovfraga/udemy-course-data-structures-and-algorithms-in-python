# Question 03 - Key with the Highest Value

# How I did it:
def max_value_key(my_dict):
    highest_value = 0
    for key in my_dict:
        if my_dict[key] > highest_value:
            highest_value = my_dict.get(key)

    highest_key = [letter for (letter, num) in my_dict.items() if num == highest_value][0]

    print(highest_key)


my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict)


# How the professor did it:
def max_value_key2(my_dict2):
    return max(my_dict2, key=my_dict2.get)


my_dict2 = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key2(my_dict2))