import array as a 
array1 = a.array('i',[1,2,3,4])

print(array1)

def accesselement(array, index):
    if index >= len(array):
        print("Out of range")
    else:
        print(array[index])

accesselement(array1,3)