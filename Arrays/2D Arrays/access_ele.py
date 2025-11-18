import numpy as np

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])

def access_ele(array,rowindex,columnindex):
    if rowindex >= len(array) or columnindex >= len(array[0]):
        print("Out of range")
    else:
        print(array[rowindex][columnindex])

access_ele(twoDarray,1,2)