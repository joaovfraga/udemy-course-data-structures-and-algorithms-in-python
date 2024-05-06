daily_temperatures = []
how_many_days = int(input("How many day's temperature? "))

for i in range(1, how_many_days + 1):
    day = int(input(f"Day {i}'s high temp: "))
    daily_temperatures.append(day)

soma_average = 0
for i in daily_temperatures:
    soma_average += i

average = soma_average / how_many_days
print(f"\nAverage = {average}")

highest_than_average = []

for i in daily_temperatures:
    if i > average:
        highest_than_average.append(i)

print(f"{len(highest_than_average)} day(s) above average")