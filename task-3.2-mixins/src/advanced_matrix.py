from __future__ import annotations
import numpy as np
from .matrix import Matrix

# Mixin for arithmetic operations
class ArithmeticMixin:
    _rows: int
    _cols: int
    matrix: list[list]
    def __add__(self, other: AdvancedMatrix):
        if self._rows != other.rows or self._cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = np.add(self.matrix, other.matrix)
        return AdvancedMatrix(result.tolist())

    def __sub__(self, other: AdvancedMatrix):
        if self._rows != other.rows or self._cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for subtraction")
        result = np.subtract(self.matrix, other.matrix)
        return AdvancedMatrix(result.tolist())

    def __mul__(self, other: AdvancedMatrix):
        if self._rows != other.rows or self._cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for component-wise multiplication")
        result = np.multiply(self.matrix, other.matrix)
        return AdvancedMatrix(result.tolist())

    def __matmul__(self, other: AdvancedMatrix):
        if self._cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")
        result = np.dot(self.matrix, other.matrix)
        return AdvancedMatrix(result.tolist())

# Mixin for file operations
class FileMixin:
    matrix: list[list]
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.matrix:
                f.write("\t".join(map(str, row)) + "\n")

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            matrix = [list(map(int, line.strip().split("\t"))) for line in f]
        return cls(matrix)

# Mixin for display
class DisplayMixin:
    matrix: list[list]
    def __str__(self):
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

# Mixin for access methods
class AccessMixin:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, value):
        self._matrix = value
        self.rows = len(value)
        self.cols = len(value[0])

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value):
        self._cols = value

class AdvancedMatrix(FileMixin, ArithmeticMixin, DisplayMixin, AccessMixin, Matrix):
    def __init__(self, matrix):
        self.matrix = matrix