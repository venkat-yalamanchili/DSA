import numpy as np 

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
newtwoDarray = np.insert(twoDarray,1,[10,11,12],axis=1)
print(twoDarray)
print(newtwoDarray)