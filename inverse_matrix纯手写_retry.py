def matrix_multiply(A, B):
    m=len(A)
    n=len(A[0])
    n2=len(B)
    p=len(B[0])
    """首先要有基础算式才能进行逆运算 因为逆运算依旧要使用这个算式"""
    if  n  !=  n2:
        raise ValueError
    C=[[0.0]  *  p for _ in range(m)]

    for i in range(m):
            for j in range(p):
                s = 0.0
                for k in range(n):
                    s  +=  A[i][k]  *  B[k][j]
            C[i][j]  =  s
    return C
def determinant_2x2(A):
    return A[0][0]  *  A[1][1]  -  A[0][1]  *  A[1][0]

def inverse_2x2 (A):
    det=determinant_2x2(A)
    """这里就是用来判断行列式 数据是不是0 如果为零那么矩阵不可逆 如果看不懂建议先去从数学方面完整学习矩阵乘法与可逆"""
    if det == 0:
        raise ValueError("矩阵不可逆")
    return [
    [A[1][1] / det, -A[0][1] / det],
        [-A[1][0] / det,  A[0][0] / det]
    ]
"""这里是逆矩阵 因为矩阵运算没有除法所以需要用乘法来代替除法的作用"""
if __name__ == "__main__":
    A=[[3,2],[1,1]]
    b=[[18],[7]]
    det = determinant_2x2(A)
    print(f"行列式: {det}")

    if det == 0:
        print("矩阵不可逆，无法求解唯一解")
    else:
        A_inv = inverse_2x2(A)
        print("逆矩阵 A⁻¹:")
        for row in A_inv:
            print(row)

        x = matrix_multiply(A_inv, b)
        print("方程组的解 x:")
        for row in x:
            print(row[0])

        b_check = matrix_multiply(A, x)
        print("验证 A·x:")
        for row in b_check:
            print(row[0])

        equal = all(abs(b_check[i][0] - b[i][0]) < 1e-10 for i in range(len(b)))
        print(f"结果是否正确: {equal}")
        """还是一样缩进与一些瑕疵 调整了十几分钟"""