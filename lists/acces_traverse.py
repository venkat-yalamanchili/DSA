integers = [1,2,3,4,5,6,7]

print(integers[0])

# for i in integers:
#     print(i)

for i in range(len(integers)):
    integers[i] = integers[i]*10

print(integers) 