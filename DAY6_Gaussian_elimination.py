def solve_linear_system(A, b):

    n = len(A)

    # 前向消元
    for i in range(n):
        # ========== 第一步：选主元并交换 ==========
        # 1. 先假设当前行i就是“老大”
        max_row = i
        # 2. 从i+1行往下找，看看谁在这一列的数字更大
        for k in range(i + 1, n):
            # 比较的是矩阵A里的数字，A[k][i]就是第k行第i列
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k

        # 3. 如果找到了新的老大，就交换
        if max_row != i:
            # 交换A的两行
            A[i], A[max_row] = A[max_row], A[i]
            # 交换b对应的两个元素
            b[i], b[max_row] = b[max_row], b[i]
            print(f"选了主元后，交换了第{i}行和第{max_row}行")

        for k in range(i + 1, n):
                factor = A[k][i] / A[i][i]
                for j in range(i , n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]
    x = [0.0] * n

                # 最后一行直接求解
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

                # 从倒数第二行开始，往上回代
    for i in range(n - 2, -1, -1):
        sum_ax = 0.0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]
    return x

if __name__ == "__main__":
    # 测试：用之前讨论过的希尔伯特矩阵（小数近似版）
    A = [[1.000, 0.500, 0.333],
         [0.500, 0.333, 0.250],
         [0.333, 0.250, 0.200]]
    b = [1.000, 0.000, 0.000]

    x = solve_linear_system(A, b)
    print("解向量 x =", x)
    print(x)