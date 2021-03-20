# Stage 4. Transpose matrix.

import numpy

class Matrix:
    def __init__(self, row, col):
        self.row = int(row)
        self.col = int(col)
        self.matrix = []

    def get_matrix(self):
        i = 1
        while i <= int(self.row):
            matr = list(map(float, input().split()))
            self.matrix.append(matr)
            i += 1


def clear_list(*full_lists):
    for i in full_lists:
        i.clear()

def matrix_enter(choice):

    if choice == 2:
        row1, col1 = input("Enter the size of matrix: ").split()
        matrix_1.row, matrix_1.col = row1, col1
        print("Enter matrix: ")
        matrix_1.get_matrix()

    if choice == 1 or choice == 3:
        row1, col1 = input("Enter the size of first matrix: ").split()
        matrix_1.row, matrix_1.col = row1, col1
        print("Enter first matrix: ")
        matrix_1.get_matrix()

        row2, col2 = input("Enter the size of second matrix: ").split()
        matrix_2.row, matrix_2.col = row2, col2
        print("Enter second matrix: ")
        matrix_2.get_matrix()

    if choice == 4:
        # To add specific menu
        print("1. Main diagonal")
        print("2. Side diagonal")
        print("3. Vertical line")
        print("4. Horizontal line")
        choice_t = int(input("Your choice: "))
        row1, col1 = input("Enter matrix size: ").split()
        matrix_1.row, matrix_1.col = row1, col1
        print("Enter matrix: ")
        matrix_1.get_matrix()
        return choice_t        

    if choice == 5 or choice == 6:
        row1, col1 = input("Enter matrix size: ").split()
        matrix_1.row, matrix_1.col = row1, col1
        print("Enter matrix: ")
        matrix_1.get_matrix()


matrix_1 = Matrix(0, 0)
matrix_2 = Matrix(0, 0)
choice = None
matrix_res = []
matrix_res2 = []

while choice != 0:
    print("\n1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("5. Calculate a determinant")
    print("6. Inverse matrix")
    print("0. Exit")
    choice = int(input("Your choice: "))

    if choice == 1:
        matrix_enter(choice)

        if matrix_1.col != matrix_2.col or matrix_1.row != matrix_2.row:
            print('The operation cannot be performed.')
        else:
            print("The result is: ")
            for h in range(int(matrix_1.row)):
                matrix_res.append([0] * int(matrix_1.col))

            for a in range(int(matrix_1.row)):
                for b in range(int(matrix_1.col)):
                    matrix_res[a][b] = matrix_1.matrix[a][b] + matrix_2.matrix[a][b]   

            for _ in matrix_res:
                print(*_)

        clear_list(matrix_1.matrix, matrix_2.matrix, matrix_res)

    if choice == 2:
        matrix_enter(choice)
        constant = int(input("Enter constant: "))

        for h in range(int(matrix_1.row)):
            matrix_res.append([0] * int(matrix_1.col))

        for a in range(int(matrix_1.row)):
            for b in range(int(matrix_1.col)):
                matrix_res[a][b] = matrix_1.matrix[a][b] * constant   

        print("The result is: ")
        for _ in matrix_res:
            print(*_)

        clear_list(matrix_1.matrix, matrix_res)

    if choice == 3:
        matrix_enter(choice)

        if matrix_1.col != matrix_2.row:
            print('The operation cannot be performed.')
        else:
            print("The result is: ")
            for h in range(int(matrix_1.row)):
                matrix_res.append([0] * int(matrix_2.col))

            for a in range(int(matrix_1.row)):
                for b in range(int(matrix_2.col)):
                    for c in range(int(matrix_2.row)):
                        matrix_res[a][b] += matrix_1.matrix[a][c] * matrix_2.matrix[c][b]   

            for _ in matrix_res:
                print(*_)

        clear_list(matrix_1.matrix, matrix_2.matrix, matrix_res)

    if choice == 4:
        choice_t = matrix_enter(choice)
        
        print("The result is: ")
        for h in range(int(matrix_1.col)):
            matrix_res.append([0] * int(matrix_1.row))

        if choice_t == 1:
            for i in range(int(matrix_1.row)):
                for j in range(int(matrix_1.col)):
                    matrix_res[j][i] = matrix_1.matrix[i][j]

        if choice_t == 2:
            for i in range(int(matrix_1.row)):
                for j in range(int(matrix_1.col)):
                    matrix_res[j][i] = matrix_1.matrix[i][j]

            for i in range(int(len(matrix_res))):
                matrix_res[i][::1] = matrix_res[i][::-1]

            
            for i in reversed(range(len(matrix_res))):
                matrix_res2.append(matrix_res[i][::1])
                
            #print(matrix_res2)
            matrix_res = matrix_res2.copy()

        if choice_t == 3:
            for i in range(int(matrix_1.row)):
                matrix_res[i][::1] = matrix_1.matrix[i][::-1]

        if choice_t == 4:
            for i in reversed(range(int(matrix_1.row))):
                matrix_res2.append(matrix_1.matrix[i][::1])
                matrix_res = matrix_res2.copy()

        for _ in matrix_res:
            print(*_)

        clear_list(matrix_1.matrix, matrix_res, matrix_res2)

    if choice == 5:
        matrix_enter(choice)
        result = 0

        if int(matrix_1.row) == 1:
            result = matrix_1.matrix[0][0]

        #Matrix 2x2
        if int(matrix_1.row) == 2:
            result = matrix_1.matrix[0][0] * matrix_1.matrix[1][1]
            result -= (matrix_1.matrix[0][1] * matrix_1.matrix[1][0])

        # Matrix 3x3
        if int(matrix_1.row) >= 3:
            m = numpy.array(matrix_1.matrix)
            result = round(numpy.linalg.det(m), 2)

        print("The result is: ")
        print(result)

        clear_list(matrix_1.matrix, matrix_res, matrix_res2)

    if choice == 6:
        matrix_enter(choice)
        m = numpy.array(matrix_1.matrix)
        inv_m = numpy.linalg.inv(m)

        print("The result is: ")
        for _ in inv_m:
            print(*_)




