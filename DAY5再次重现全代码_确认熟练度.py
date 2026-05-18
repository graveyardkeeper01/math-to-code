from 练习.inverse_matrix import A_inv


def matrix_multiply(A, B):
    m = len(A)
    n = len(A[0])
    n2 = len(B)
    p = len(B[0])


    if n != n2:
        raise ValueError("矩阵尺寸错误")

    C  =[ [0.0]  *  p   for _ in range(m)]
    for i in range (m):
        for j  in range(p):
            s = 0.0
            for k  in range(n):
                s += A[i][k] * B[k][j]

            C[i][j] = s
    return  C
def determinant2x2(A):
    return A[1][1] * A[0][0] - A[0][1]  *  A[1][0]

def inverse_2x2(A):
    det = determinant2x2(A)
    if det == 0.0:
        raise ValueError("阵列式为零不可逆")

    return [


        [A[1][1]/det,-A[0][1]/det],
        [-A[1][0]/det,A[0][0]/det]
    ]

if __name__ == "__main__":
    A=[[5,10],
       [11,8]]
    B=[[18],
       [20]]

    det  = determinant2x2(A)
    print(det)
    A_inv=inverse_2x2(A)
    print(A_inv)

    x=matrix_multiply(A_inv,B)
    print(x)
