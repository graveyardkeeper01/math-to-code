import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)
b=np.array([[10,11,12],[13,14,15],[16,17,18]],dtype=float)

Q,R=np.linalg.qr(A)
Q=Q[:,:A.shape[1]]
R=R[:A.shape[1],:]

x=np.linalg.solve(R,Q.T@b)
print(x)
