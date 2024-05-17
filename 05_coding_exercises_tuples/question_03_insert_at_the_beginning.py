# Question 03 - Insert at the Beginning

def insert_value_front(in_tuple, insert):
    return (insert,) + in_tuple


input_tuple = (2, 3, 4)
value_to_insert = 1

output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)