# Professor solution with Array

how_many_days = int(input("How many day's temperature? "))

total = 0
temp = []
for i in range(how_many_days):
    nextDay = int(input("Day " + str(i + 1) + "'s high temp: "))
    temp.append(nextDay)
    total += temp[i]

avg = round(total / how_many_days, 2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + "day(s) above average")