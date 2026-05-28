
import numpy as np

def classical_gram_schmidt(A):
    m,n=A.shape
    Q = np.zeros((m,n))
    R = np.zeros((n,n))

    for j in range(n):
        v=A[:,j].copy()
        for i in range(j):
            R[i,j]=np.dot(Q[:,i],A[:,j])
            v=v-R[i,j] * Q[:,i]
            Q[:,j]=v/R[j,j]

        return Q,R

def qr_algorithm(A,num_iter=100,tol=1e-12):

    A_k = A.copy().astype(float)

    for _ in range(num_iter):

        Q,R = classical_gram_schmidt(A_k)

        A_k = R @ Q

    return np.diag(A_k)

if __name__=='__main__':
    A = np.array([[2,1],
                  [1,2]],dtype=float)
    eigenvalues=qr_algorithm(A)
    print(eigenvalues)
    print(np.linalg.eigvals(A))

