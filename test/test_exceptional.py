import unittest
from mainclass import MatrixOperations
from test.TestUtils import TestUtils
import numpy as np

class ExceptionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.matrix_a = np.array([[1, 2], [3, 4]])
        self.matrix_b = np.array([[5, 6, 7], [8, 9, 10], [11, 12, 13]])
        self.matrix_operations = MatrixOperations(self.matrix_a, self.matrix_b)

    def test_invalid_matrix_multiplication(self):
        """Test if ValueError is raised for incompatible matrix dimensions"""
        test_obj = TestUtils()
        try:
            self.matrix_operations.matrix_multiplication()
            test_obj.yakshaAssert("TestInvalidMatrixMultiplication", False, "exceptional")
            print("TestInvalidMatrixMultiplication = Failed")
        except ValueError as e:
            if str(e) == "Matrix A columns must match Matrix B rows for multiplication":
                test_obj.yakshaAssert("TestInvalidMatrixMultiplication", True, "exceptional")
                print("TestInvalidMatrixMultiplication = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidMatrixMultiplication", False, "exceptional")
                print("TestInvalidMatrixMultiplication = Failed")

    def test_determinant_of_non_square_matrix(self):
        """Test if error is raised for non-square matrix when calculating determinant"""
        matrix_c = np.array([[1, 2, 3], [4, 5, 6]])
        test_obj = TestUtils()
        try:
            self.matrix_operations.determinant("matrix_c")
            test_obj.yakshaAssert("TestDeterminantOfNonSquareMatrix", False, "exceptional")
            print("TestDeterminantOfNonSquareMatrix = Failed")
        except ValueError as e:
            test_obj.yakshaAssert("TestDeterminantOfNonSquareMatrix", True, "exceptional")
            print("TestDeterminantOfNonSquareMatrix = Passed")
