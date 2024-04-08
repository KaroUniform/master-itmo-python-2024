from matrix import Matrix

class MatrixHashMixin:
    """
    A mixin to add hashing capability to the Matrix class.
    It provides a method to calculate a hash value based on the matrix's elements.
    """
    
    matrix: list[list]
    
    # Correct (?) hash but really hard to crack
    # def __hash__(self):
    #     matrix_string = "".join(str(item) for row in self.matrix for item in row)
    #     return hash(matrix_string)
    
    # Hash with vulnerability
    def __hash__(self):
        return sum(item for row in self.matrix for item in row)


class AdvancedMatrix(MatrixHashMixin, Matrix):
    
    _mul_cache = {}

    def __matmul__(self, other):
        cache_key = (hash(self), hash(other))
        if cache_key in AdvancedMatrix._mul_cache:
            return AdvancedMatrix._mul_cache[cache_key]
        if self.cols != other.rows:
            raise ValueError("The number of columns in the first matrix must be equal to the number of rows in the second for matrix multiplication")
        result = [[sum(a * b for a, b in zip(self_row, other_col)) for other_col in zip(*other.matrix)] for self_row in self.matrix]
        AdvancedMatrix._mul_cache[cache_key] = AdvancedMatrix(result)
        return AdvancedMatrix._mul_cache[cache_key]