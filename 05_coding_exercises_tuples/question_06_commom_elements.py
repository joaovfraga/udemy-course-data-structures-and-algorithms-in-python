# Question 06 - Commom Elements

# My Solution:
def common_elements(tuple1, tuple2):
    my_list = []
    for num1 in tuple1:
        for num2 in tuple2:
            if num1 == num2:
                my_list.append(num1)

    my_tuple = tuple(my_list)

    return my_tuple


# Professor Solution:
def common_elements2(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
