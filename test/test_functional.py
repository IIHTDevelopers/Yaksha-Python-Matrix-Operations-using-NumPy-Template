import unittest
import numpy as np
from mainclass import MatrixOperations
from test.TestUtils import TestUtils


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.matrix_a = np.array([[1, 2], [3, 4]])
        self.matrix_b = np.array([[5, 6], [7, 8]])
        self.matrix_operations = MatrixOperations(self.matrix_a, self.matrix_b)

    def test_dot_product(self):
        """Test if dot product is calculated correctly"""
        obj = self.matrix_operations.dot_product()
        expected_dot_product = np.array([[19, 22], [43, 50]])
        test_obj = TestUtils()
        if np.array_equal(obj, expected_dot_product):
            test_obj.yakshaAssert("TestDotProduct", True, "functional")
            print("TestDotProduct = Passed")
        else:
            test_obj.yakshaAssert("TestDotProduct", False, "functional")
            print("TestDotProduct = Failed")

    def test_matrix_multiplication(self):
        """Test if matrix multiplication is calculated correctly"""
        obj = self.matrix_operations.matrix_multiplication()
        expected_multiplication = np.array([[19, 22], [43, 50]])
        test_obj = TestUtils()
        if np.array_equal(obj, expected_multiplication):
            test_obj.yakshaAssert("TestMatrixMultiplication", True, "functional")
            print("TestMatrixMultiplication = Passed")
        else:
            test_obj.yakshaAssert("TestMatrixMultiplication", False, "functional")
            print("TestMatrixMultiplication = Failed")
