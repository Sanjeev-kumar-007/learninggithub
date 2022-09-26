import numpy as np


def matmult(m1, m2):

    sums = 0
    mat1 = np.array(m1)


    mat2 = np.array(m2)

    dim_mat1 = mat1.shape
    dim_mat2 = mat2.shape

    result = np.array([[0] * dim_mat2[1]] * dim_mat1[0])

    if dim_mat1[1] == dim_mat2[0]:
        for i in range(0, dim_mat1[0], 1):
            for j in range(0, dim_mat2[1], 1):
                for k in range(0, dim_mat1[1], 1):
                    sums = sums + mat1[i][k] * mat2[k][j]
                result[i][j] = sums
                sums = 0

        return result
    else:
        print("Matrix multiplication is not possible as dimension do not match")





for x in range(2):
    mat=[]
    r = int(input("Enter the number of Rows:"))
    c= int(input("Enter the number of columns:"))

    for i in range(r):
        inu = []
        for j in range(c):
            n= int(input())
            inu.append(n)
        mat.append(inu)

    if x == 0:
        a = mat
    else:
        b = mat


c = matmult(a,b)
print("The product of the two matrix is ","\n",c)