import numpy as np
def power_iteration(A,num_iter=100,tol=1e-12):
    n=A.shape[0]
    v1=np.random.randn(n)
    v1=v1/np.linalg.norm(A)

    for _ in range(num_iter):
        v2=np.dot(A,v1)
        v2=v2/np.linalg.norm(v2)

        eignvalue=np.dot(v2,np.dot(A,v2))

        if np.linalg(v2) <tol:
            break

        v1=v2
        return eignvalue,v2