# Stage 1. Matrix multiplication.

class Matrix:
    def __init__(self, row, col):
        self.row = int(row)
        self.col = int(col)
        self.matrix = []

    def get_matrix(self):
        i = 1
        while i <= self.row:
            matr = list(map(float, input().split()))
            self.matrix.append(matr)
            i += 1

def clear_list(*full_lists):
    for i in full_lists:
        i.clear()


choice = None
while choice != 0:
    print("\n1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("0. Exit")
    choice = int(input("Your choice: "))

    if choice == 1:
        row1, col1 = input("Enter the size of first matrix: ").split()
        matrix_1 = Matrix(row1, col1)
        print("Enter first matrix: ")
        matrix_1.get_matrix()

        row2, col2 = input("Enter the size of second matrix: ").split()
        matrix_2 = Matrix(row2, col2)
        print("Enter second matrix: ")
        matrix_2.get_matrix()

        matrix_res = []
        if col1 != col2 or row1 != row2:
            print('The operation cannot be performed.')
        else:
            print("The result is: ")
            for h in range(int(row1)):
                matrix_res.append([0] * int(col1))

            for a in range(int(row1)):
                for b in range(int(col1)):
                    matrix_res[a][b] = matrix_1.matrix[a][b] + matrix_2.matrix[a][b]   

            for _ in matrix_res:
                print(*_)

        clear_list(matrix_1.matrix, matrix_2.matrix, matrix_res)

    if choice == 2:
        row1, col1 = input("Enter the size of matrix: ").split()
        matrix_1 = Matrix(row1, col1)
        print("Enter matrix: ")
        matrix_1.get_matrix()
        constant = int(input("Enter constant: "))
        matrix_res = []

        for h in range(int(row1)):
            matrix_res.append([0] * int(col1))

        for a in range(int(row1)):
            for b in range(int(col1)):
                matrix_res[a][b] = matrix_1.matrix[a][b] * constant   

        print("The result is: ")
        for _ in matrix_res:
            print(*_)

        clear_list(matrix_1.matrix, matrix_res)

    if choice == 3:
        row1, col1 = input("Enter the size of first matrix: ").split()
        matrix_1 = Matrix(row1, col1)
        print("Enter first matrix: ")
        matrix_1.get_matrix()

        row2, col2 = input("Enter the size of second matrix: ").split()
        matrix_2 = Matrix(row2, col2)
        print("Enter second matrix: ")
        matrix_2.get_matrix()

        matrix_res = []
        if col1 != row2:
            print('The operation cannot be performed.')
        else:
            print("The result is: ")
            for h in range(int(row1)):
                matrix_res.append([0] * int(col2))

            for a in range(int(row1)):
                for b in range(int(col2)):
                    for c in range(int(row2)):
                        matrix_res[a][b] += matrix_1.matrix[a][c] * matrix_2.matrix[c][b]   

            for _ in matrix_res:
                print(*_)

        clear_list(matrix_1.matrix, matrix_2.matrix, matrix_res)


