list = []

while True:
    val = input("Enter number(press 'q' to quit)")
    if val == "q": break
    num = float(val)
    list.append(num)

print(f"Average of given numbers is {sum(list)/len(list)}")