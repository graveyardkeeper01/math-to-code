import numpy as np
def classical_gram_schmidt(A):

    m,n=A.shape
    Q=np.zeros((m,n))
    R=np.zeros((m,n))
    for j in range(m):
        v = A[:,j].copy()
        for i in range(j):
            R[i,j]=np.dot(A[:,i],Q[:,i])
            """代码计算过程中先计算R的系数，在回头求解"""
            """同时没有计算，R左下角数值由于之前的零填充自然为0"""
            v=v-R[i,j]  * Q[:,i]
            R[j,j]= np.linalg.norm(v)
            Q[:,j]=v/R[j,j]

        return Q,R