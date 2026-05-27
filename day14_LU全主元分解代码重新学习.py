def full_pivot(A):
    n=len(A)
    U=[row[:] for row in A]

    L=[[0.0] * n for _ in range(n)]
    for i in range(n):
        L[i][i]=1.0
        P=list(range(n))
        Q=list(range(n))

        for k in range(n):
            max_val=-1.0
            r,c=k,k
            for i in range(k,n):
                for j in range(k,n):
                    if abs(U[i][j]) > max_val:
                        max_val=abs(U[i][j])
                        r,c=i,j

            if max_val < 1e-12:
                raise ValueError("矩阵奇异")

            if r != k:
                U[k],U[r]=U[r],U[k]
                for j in range(k):
                    L[k][j], L[r][j]=L[r][j],L[k][j]

                    P[k],P[r]=P[r],P[k]
            if c !=k:
                for i in range(n):
                    U[i][k],U[i][c]=U[i][c],U[i][k]
                Q[k],Q[c]=Q[c],Q[k]

                for i in range(k+1,n):
                    factor=U[i][k]/U[k][k]

                    L[i][k]=factor

                    for j in range(k,n):
                        U[i][j]-=factor*U[k][j]

                        Q[k],Q[c]=Q[c],Q[k]
                        return P,Q,L,U

def solve_full_pivot(P,Q,L,U,b):
    n=len(b)

    b1=[b[P[i]] for i in range(n)]
        
    y=[0.0] * n
    for i in range(n):
        s=b1[i]
        for j in range(n):
            s -=L[i][j] * y[j]
        y[i] = s
        z=[0.0] * n
        for i in range(n-1,-1,-1):
            s = y[i]
            for j in range(i+1,n):
                s -=U[i][j] * z[j]
            z[i] = s/U[i][i]
            x=[0.0] * n
            for j in range(n):
                x[Q[j]]=z[j]
            return x