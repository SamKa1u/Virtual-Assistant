import numpy as np

# LINEAR ALGEBRA
# A = np.array([[3.,-3],[-2,-5]])
# print(A)
# B = np.array([[2.,-4],[4,5]])
# # print(B)
# # C = np.add(A,B)
# c = np.array(9*A)
# b = np.array(8*B)
# a = np.subtract(c,b)
# print(a)

#MATRICES
# determiant of matrix
def Det(mtrx):
    """
        calculates determinant of given square matrix

        Args:
            mtrx np.array: matrix to calculate determinant

        Returns:
            Adet: The  determinant of the matrix.
        """
    A = mtrx
    Adet = np.linalg.det(A)
    return Adet

def round(Adet):
    """
        rounds determinant to nearest integer

        Args:
            Adet (float): determinant of A

        Returns:
            AdetRND: The rounded determinant of the matrix.
    """
    if Adet < 0:
        if abs(Adet % int(Adet)) > .5:
            AdetRND = int(Adet) - 1
        else:
            AdetRND = int(Adet)
    elif Adet > 0:
        if abs(Adet % int(Adet)) > .5:
            AdetRND = int(Adet) + 1
        else:
            AdetRND = int(Adet)
    else:
        AdetRND = Adet
    return float(AdetRND)

#Minor of matrix
def get_minor(arr, i, j):
    """
    Calculates the minor of a matrix at the given row and column.

    Args:
        arr (np.ndarray): The input matrix.
        i (int): The row index to exclude.
        j (int): The column index to exclude.

    Returns:
        np.ndarray: The minor of the matrix.
    """
    temp = arr[np.array(list(range(i)) + list(range(i + 1, arr.shape[0])))[:, np.newaxis],
               np.array(list(range(j)) + list(range(j + 1, arr.shape[1])))]

    return temp

def matrix_calc():
    start = 0
    while True:
        if start !=0:
            quit = str(input("Would you like to quit?(q):"))
            if quit.lower() == "q":
                break
        # select size of square matrix
        matrix_type = str(input("matrix dimesnsions(5x5/4x4/3x3):"))
        dims = matrix_type.lower()
        print(dims)
        if dims == "4x4":
            # get matrix from user
            a1, a2, a3, a4 = float(input("enter row 1:\n")), float(input()), float(input()), float(input())
            b1, b2, b3, b4 = float(input("enter row 2\n")), float(input()), float(input()), float(input())
            c1, c2, c3, c4 = float(input("enter row 3\n")), float(input()), float(input()), float(input())
            d1, d2, d3, d4 = float(input("enter row 4\n")), float(input()), float(input()), float(input())
            A = np.array([a1, a2, a3, a4])
            B = np.array([b1, b2, b3, b4])
            C = np.array([c1, c2, c3, c4])
            D = np.array([d1, d2, d3, d4])

            matrix = np.array([A,
                               B,
                               C,
                               D,])
        elif dims == "5x5":
            # get matrix from user
            a1, a2, a3, a4, a5 = float(input("enter row 1:\n")), float(input()), float(input()), float(input()), float(input())
            b1, b2, b3, b4, b5 = float(input("enter row 2\n")), float(input()), float(input()), float(input()), float(input())
            c1, c2, c3, c4, c5 = float(input("enter row 3\n")), float(input()), float(input()), float(input()), float(input())
            d1, d2, d3, d4, d5 = float(input("enter row 4\n")), float(input()), float(input()), float(input()), float(input())
            e1, e2, e3, e4, e5 = float(input("enter row 5\n")), float(input()), float(input()), float(input()), float(input())
            A = np.array([a1, a2, a3, a4, a5])
            B = np.array([b1, b2, b3, b4, b5])
            C = np.array([c1, c2, c3, c4, c5])
            D = np.array([d1, c2, c3, c4, c5])
            E = np.array([e1, e2, e3, e4, e5])

            # sample matrix
            # A = np.array([9,7,-8])
            # B = np.array([-3,0,-6])
            # C = np.array([-6,7,9])
            matrix = np.array([A,
                               B,
                               C,
                               D,
                               E])
        else:
            # get matrix from user
            a1, a2, a3 = float(input("enter row 1:\n")), float(input()), float(input())
            b1, b2, b3 = float(input("enter row 2\n")), float(input()), float(input())
            c1, c2, c3 = float(input("enter row 3\n")), float(input()), float(input())

            A = np.array([a1,a2,a3])
            B = np.array([b1,b2,b3])
            C = np.array([c1,c2,c3])
            #sample matrix
            # A = np.array([9,7,-8])
            # B = np.array([-3,0,-6])
            # C = np.array([-6,7,9])
            matrix = np.array([A,
                               B,
                               C])

        if dims != "4x4" and dims != "5x5":
            #finding matrix Minor
            minor_0_0 = get_minor(matrix, 0, 0)
            minor_0_1 = get_minor(matrix, 0, 1)
            minor_0_2 = get_minor(matrix, 0, 2)
            A = np.array([round(Det(minor_0_0)), round(Det(minor_0_1)), round(Det(minor_0_2))])

            minor_1_0 = get_minor(matrix, 1, 0)
            minor_1_1 = get_minor(matrix, 1, 1)
            minor_1_2 = get_minor(matrix, 1, 2)
            B = np.array([round(Det(minor_1_0)), round(Det(minor_1_1)), round(Det(minor_1_2))])

            minor_2_0 = get_minor(matrix, 2, 0)
            minor_2_1 = get_minor(matrix, 2, 1)
            minor_2_2 = get_minor(matrix, 2, 2)
            C = np.array([round(Det(minor_2_0)), round(Det(minor_2_1)), round(Det(minor_2_2))])
            m_matrix = np.array([A,
                                 B,
                                 C])
            print("Minor matrix\n", m_matrix)

            #cofactor matrix
            print("Cofactor matrix:")
            print("\n[",round(Det(minor_0_0)), -1*round(Det(minor_0_1)), round(Det(minor_0_2)))
            print("\n",-1*round(Det(minor_1_0)), round(Det(minor_1_1)), -1*round(Det(minor_1_2)),)
            print("\n",round(Det(minor_2_0)), -1*round(Det(minor_2_1)), round(Det(minor_2_2)),"]")

        # get matrix determinant
        print("Matrix determinant: ", round(Det(matrix)))
        start=1

if __name__ == "__main__":
    matrix_calc()