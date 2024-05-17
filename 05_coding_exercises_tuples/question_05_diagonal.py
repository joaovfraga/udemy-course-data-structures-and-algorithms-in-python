# Question 05 - Diagonal

def get_diagonal(tup):
    return tuple(tup[i][i] for i in range(len(tup)))


tup = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

output_tuple = get_diagonal(tup)
print(output_tuple)




