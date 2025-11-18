import array as a

#1. Create an array and traverse
my_array = a.array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

#2. Acess individual elements through indexes
for i in range(len(my_array)):
    print (my_array[i])

#3. Append any value to the array using append method
my_array.append(10)
print(my_array)

#4. Insert value in an array using insert method
my_array.insert(0,25)
print(my_array)

#5. Extend python array using extend() method
my_array2 = a.array('i',[31,32,33])
my_array.extend(my_array2)
print(my_array)

#6. Add items from list into array using fromlist() method
list1 = [12,13,14]
my_array.fromlist(list1)
print(my_array)

#7. Remove my array element using remove() method
my_array.remove(2)  # only remove 1st occurence of the element
print(my_array)

#8. Remove last array element using pop() method
my_array.pop()
print(my_array)

#9. Fetch any element through its index using index() method
print(my_array.index(33))

#10. Reverse a python array using reverse method
my_array.reverse()
print(my_array)

#11. Get array buffer information using buffer_info() method
print(my_array.buffer_info())

#12. Check no.of occurence of a element using count() method
my_array.append(1)
print(my_array.count(1))

#13. COnvert array to string using tostring() changed tobytes() method
strTemp = my_array.tobytes()
print(strTemp)
ints = a.array('i',[])
ints.frombytes(strTemp)
print(ints)

#14. COnvert array to list
print(my_array.tolist())

#15. Slice elements from an array
print(my_array[1:6])
