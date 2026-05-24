def full_pivoting(A,b):
    n = len(A)
    m = len(A[0])
    col = list(range(m))

    for i in range(min(n, m)):
        max_val = abs(A[i][i])
        max_row, max_col = i, i
        for i0 in range(i, n):
            for k0 in range(i, m):
                if abs(A[i0][k0]) > max_val:
                    max_val = abs(A[i0][k0])
                    max_row, max_col = i0, k0

        if max_val < 1e-12:
            raise ValueError("矩阵奇异，无唯一解")

        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]

    # --- 交换列 ---
        if max_col != i:
            for r in range(n):
                A[r][i], A[r][max_col] = A[r][max_col], A[r][i]
                col[i], col[max_col] = col[max_col], col[i]

            for k in range(i+1, n):
                factor=A[k][i] / A[i][i]
                for j in range(i, m):
                    A[k][j] -= factor * A[i][j]
                    b[k] -= factor * b[i]

    x = [0.0] * m
    x[m - 1] = b[m - 1] / A[m - 1][m - 1]
    for i in range(m - 2, -1, -1):
        sum_ax = 0.0
        for j in range(i + 1, m):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]

    # --- 恢复解的顺序 ---
    x1 = [0.0] * m
    for i in range(m):
        x1[col[i]] = x[i]

    return x