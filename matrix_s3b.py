# Stage 1. Matrix multiplication.

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

matrix_1 = Matrix(0, 0)
matrix_2 = Matrix(0, 0)
choice = None

while choice != 0:
    print("\n1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice: "))

    if choice == 1:
        matrix_enter(choice)

        matrix_res = []
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
        matrix_res = []

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

        matrix_res = []
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


