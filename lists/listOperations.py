mylist = [1,2,3,4,5,6,7,8]
print(mylist)

mylist[1] = 11   #Updating a list
print(mylist)

mylist.insert(0,21)
print(mylist)   # iserting at given index

mylist.append(22)
print(mylist)    #inserting at the end

newlist=[8,9,0]
mylist.extend(newlist)
print(mylist)   # joining two lists

print(mylist[0:5:2]) # slicing the list same logic as string slicing

mylist.pop(0) # deletes element at index 0
print(mylist) # if you dont give any index it deletes element at the end

del mylist[0:2] # deletes multiple elements from the list using slicing
print(mylist)

mylist.remove(22) # removes the given element (its useful if we know the element itself)
print(mylist)