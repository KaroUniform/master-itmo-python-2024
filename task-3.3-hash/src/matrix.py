#
# Нужно реализовать небольшую библиотеку для работы с матрицами
# Сделать класс матрицы, в котором определить операции сложения и умножения (матричного и покомпонентного) через перегрузку операторов +, *, @ (как в numpy). Вызывать исключения, если матрицы на входе некорректной размерности (ValueError)
#


class Matrix:
    """
    A class representing a matrix and supporting basic matrix operations.

    Args:
        matrix (list[list]): A 2D list representing the matrix.

    Attributes:
        matrix (list[list]): The 2D list representing the matrix.
        rows (int): The number of rows in the matrix.
        cols (int): The number of columns in the matrix.

    Methods:
        __init__: Initializes the Matrix object.
        __str__: Returns a string representation of the matrix.
        __add__: Adds two matrices element-wise.
        __mul__: Performs component-wise multiplication of two matrices.
        __matmul__: Performs matrix multiplication of two matrices.
    """

    def __init__(self, matrix):
        """
        Initializes the Matrix object with the given matrix.

        Args:
            matrix (list[list]): A 2D list representing the matrix.
        """
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        """
        Returns a string representation of the matrix.

        Returns:
            str: String representation of the matrix.
        """
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        """
        Adds two matrices element-wise.

        Args:
            other (Matrix): The matrix to be added.

        Returns:
            Matrix: A new Matrix object representing the result of the addition.
        
        Raises:
            ValueError: If matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for addition")
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __mul__(self, other):
        """
        Performs component-wise multiplication of two matrices.

        Args:
            other (Matrix): The matrix to be multiplied.

        Returns:
            Matrix: A new Matrix object representing the result of the multiplication.
        
        Raises:
            ValueError: If matrices have different dimensions.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices must have the same dimensions for component-wise multiplication")
        result = [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        return Matrix(result)

    def __matmul__(self, other):
        """
        Performs matrix multiplication of two matrices.

        Args:
            other (Matrix): The matrix to be multiplied.

        Returns:
            Matrix: A new Matrix object representing the result of the multiplication.
        
        Raises:
            ValueError: If the number of columns in the first matrix is not equal to the number of rows in the second matrix.
        """
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")
        result = [[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other.matrix)] for self_row in self.matrix]
        return Matrix(result)

    