newtuple = (1,2,3,4,5)

# for i in newtuple:
#     print(i)

value = 3
for i in range(len(newtuple)):     # searching in a tuple
    if newtuple[i] == value:
        print(i)


print(newtuple.index(5)) #to get the index of the given value