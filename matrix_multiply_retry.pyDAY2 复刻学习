from cmath import infj

import p


def matrix_multiply(A,B):

    m  =  len(A)
    n  =  len(A[0])
    n2  =  len(B)
    p  =  len(B[0])
    if  n  != n2 :
            raise ValueError("矩阵尺寸不匹配")
    """这里其实都没什么问题最重要的问题是缩进，我属于零基础不熟悉基础要求正常。"""
    C=[[0.0]  * p for _ in  range  (m)]

    for   i  in   range(m):
        for j  in   range(p):
            s =0.0
            for k in range(n):
                s  +=  A[i][k]  *  B[k][j]
            C[i][j]   =   s
    return  C

if __name__ == '__main__':
    A=[[1,2],[3,4]]
    B=[[5,6],[7,8]]
    C_hand=matrix_multiply(A,B)
print("手写矩阵方程=")
for row in  C_hand:
        print(row)
"""我在过程中节省了很多，就比如测试运行什么的，还有第一句引用验证函数，其次非常不熟练，基本是写一句看三眼，但是我感觉我是理解这串代码的
然后就是数学方面，你要是问我矩阵乘法是怎么运行的怎么计算的我可以告诉你，但是你把公式扔给我我是看不懂的。也说明数学基础很差，有点好玩，懂但是又不懂"""
