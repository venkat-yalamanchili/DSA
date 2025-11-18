a = int(input("How many days temperature? "))
temp = []

for i in range(1,a+1):
    value = float(input(f"Enter day {i} temperature: "))
    temp.append(value)

Avg = sum(temp)/len(temp)

count = 0
for i in temp:
    if i > Avg:
        count +=1

print(f"Average: {Avg}")
print(f"{count} day/s above average")