import numpy as np
def classical_gram_schmidt(A):
    m,n = A.shape
    Q=np.zeros((m,n))
    R=np.zeros((m,n))

    for j in range(n):
        v = A[:,j].copy()

        for i in range(j):
            R[i,j] = np.dot(Q[:,i],A[:,j])
            v= v - R[i,j]  * Q[:,i]

        R[j,j]=np.linalg.norm(v)
        Q[:,j]=v/R[j,j]

    return Q,R