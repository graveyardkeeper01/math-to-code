def full_pivot_lu(A,b):
    m = len(A)
    n = len(A[0])
    col =list(range(m))

    for i in range(m):
        max_val = abs(A[i][i])
        max_row =i , max_col= i

        if abs(A[i][i])<abs(A[max_row][max_col]):
                max_row=i
                max_col=j
                max_val=A[i][j]

                if max_val <1e-12:
                    raise ValueError("矩阵奇异，不可逆")

                if max_row !=i:
                    max_row=c
                    A[i],A[max_row] = A[max_row],A[i]
                    b[i],b[max_row] =b[max_row],A[i]
                if max_col !=j:
                    max_col=r
                    A[r],A[max_col] = A[max_col],A[r]
                    b[r] ,b[max_col] = b[max_col],A[r]
