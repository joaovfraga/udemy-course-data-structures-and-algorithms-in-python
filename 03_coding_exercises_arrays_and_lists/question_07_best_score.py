# QUESTION 07 - Best Score
#  Given a list, write a function to get first, second best scores from the list.
#  List may contain duplicates.

def first_second(my_list):
    best1 = 0
    best2 = 0

    for score in my_list:
        if score > best1:
            best2 = best1
            best1 = score
        elif score > best2:
            best2 = score

    return best1, best2


myList = [84, 85, 86, 87, 85, 90, 85, 83, 23, 45, 84, 1, 2, 0]
print(first_second(myList))
