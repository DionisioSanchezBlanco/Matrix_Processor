# Stage 1. Matrix multiplication.

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
constant = int(input())

matrix_res = []

for h in range(int(row1)):
    matrix_res.append([0] * int(col1))

for a in range(int(row1)):
    for b in range(int(col1)):
        matrix_res[a][b] = matrix_1.matrix[a][b] * constant   

for _ in matrix_res:
    print(*_)
