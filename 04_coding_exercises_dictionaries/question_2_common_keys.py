# Question 02 - Common Keys

# How I did it:
def merge_dicts(dict1, dict2):
    new_dic = {}
    for key in dict1:
        if key in dict2:
            new_dic[key] = dict1[key] + dict2[key]
        else:
            new_dic[key] = dict1[key]
            new_dic.update(dict2)

    print(new_dic)


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

merge_dicts(dict1, dict2)


# How the professor did it:
def merge_dicts2(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(merge_dicts2(dict1, dict2))
