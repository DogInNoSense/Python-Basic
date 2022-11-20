import numpy as np
A = [[1,-1],[-2,2],[2,-2]]

x,y,z = np.linalg.svd(A)
print(x,y,z)