class Matrix:
    def __new__(cls, *args):
        instance=object.__new__(cls)
        return instance

    def __init__(self, rows, cols, value=0):
        self.rows=rows
        self.cols=cols
        self.matr=([[value]*self.cols]*self.rows)

    def get_value(self, row, col):
        pass

    def set_value(self, row, col, value):
        pass

    def __repr__(self):
        return f'{self.__class__.__name__}({self.rows}, {self.cols})'

    def __str__(self):
        return f'0 0 0\n0 0 0'

print(Matrix(2, 3))
# matrix=Matrix(2,3)
# print(*[i for i in matrix.matr], sep='\n')