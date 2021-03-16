# Stage 1. Matrix processor.

class Matrix:
    def __init__(self, row, col):
        self.row = int(row)
        self.col = int(col)
        self.matrix = []

    def get_matrix(self):
        i = 1
        while i <= self.row:
            matr = list(map(int, input().split()))
            self.matrix.append(matr)
            i += 1


row1, col1 = input().split()
matrix_1 = Matrix(row1, col1)
matrix_1.get_matrix()

row2, col2 = input().split()
matrix_2 = Matrix(row2, col2)
matrix_2.get_matrix()

matrix_res = []

if col1 != col2 or row1 != row2:
    print('ERROR')
else:
    for h in range(int(row1)):
        matrix_res.append([0] * int(col1))

    for a in range(int(row1)):
        for b in range(int(col1)):
            matrix_res[a][b] = matrix_1.matrix[a][b] + matrix_2.matrix[a][b]   

    for _ in matrix_res:
        print(*_)
