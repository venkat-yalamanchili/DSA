import numpy as np

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])

def search_ele(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == target:
                return i,j
    return "Element not found"

print(twoDarray)
print(search_ele(twoDarray,12))