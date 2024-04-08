import unittest
import numpy as np
from src.matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_addition(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[5, 6], [7, 8]])
        expected = np.array([[6, 8], [10, 12]])
        result = A + B
        self.assertTrue(np.array_equal(result.matrix, expected))

    def test_component_wise_multiplication(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[2, 3], [4, 5]])
        expected = np.array([[2, 6], [12, 20]])
        result = A * B
        self.assertTrue(np.array_equal(result.matrix, expected))

    def test_matrix_multiplication(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[2, 0], [1, 2]])
        expected = np.array([[4, 4], [10, 8]])
        result = A @ B
        self.assertTrue(np.array_equal(result.matrix, expected))

    def test_addition_dimension_mismatch(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        with self.assertRaises(ValueError):
            _ = A + B

    def test_component_wise_multiplication_dimension_mismatch(self):
        A = Matrix([[1, 2], [3, 4]])
        B = Matrix([[1]])
        with self.assertRaises(ValueError):
            _ = A * B

    def test_matrix_multiplication_dimension_mismatch(self):
        A = Matrix([[1, 2, 3]])
        B = Matrix([[1, 2], [3, 4]])
        with self.assertRaises(ValueError):
            _ = A @ B

if __name__ == '__main__':
    unittest.main()
