import numpy as np

twoDarray = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(twoDarray)
newtwoDarray = np.delete(twoDarray,1,axis=0)
print(newtwoDarray) 