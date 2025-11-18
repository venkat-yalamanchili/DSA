import array as a 

array1 = a.array('i',[20,45,67,34,64])

def search_element(array,tar):
    for i in range(len(array)):
        if array[i] == tar:
            return i
    return -1

print(search_element(array1,67))