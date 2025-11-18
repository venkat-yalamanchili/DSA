import numpy as np

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDarray)

for i in range(len(twoDarray)):
    for j in range(len(twoDarray[0])):
        print(twoDarray[i][j])