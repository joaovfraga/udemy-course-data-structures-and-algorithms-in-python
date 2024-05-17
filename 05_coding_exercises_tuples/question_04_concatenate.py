# Question 04 - Concatenate

# My Solution - Which didn't work cause there was a black space at the end of the new string
def concatenate_strings2(input_tuple):
    new_string = ""
    for word in input_tuple:
        new_string = new_string + word + " "
    return new_string


# Professor Solution:
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)


input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)
