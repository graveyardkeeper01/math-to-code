import numpy as np
import matplotlib.pyplot as plt

from 练习.DAY11_gram_schmidt import classical_gram_schmidt


def calssical_gram_schmidt(A):
    m,n=A.shape
    Q=np.zeros((m,n))
    R=np.zeros((n,n))
    for j in range(n):
        v=A[:,j].copy()
        for i in range(j):
            R[i,j] = np.dot(Q[:,i],A[:,j])
            v= v-R[i,j] * Q[:,j]

        R[j,j] =np.linalg.norm(v)
        Q[:,j] = v / R[j,j]
    return Q,R
def back_substitute(R,Qb):
    n=len(R)
    x=np.zeros(n)
    for i in range(n-1,-1,-1):
        x[i]=(Qb[i]-np.dot(R[i,i+1:],x[i+1:]))
    return x

np.random.seed(42)
x=np.linspace(1,10,50)
y=3*x+np.random.normal(0,2,size=len(x))
A=np.column_stack([x,np.ones_like(x)])
Q,R=calssical_gram_schmidt(A)

Qb=Q.T @ y
coefficients = back_substitute(R,Qb)


print("回归系数:", coefficients)
print("NumPy验证:", np.linalg.lstsq(A, y, rcond=None)[0])



plt.scatter(x, y, alpha=0.6, label='Data')
plt.plot(x, coefficients[0] * x + coefficients[1], 'r-', label='My QR Regression')
plt.legend()
plt.show()
