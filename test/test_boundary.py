import unittest
import numpy as np
from mainclass import MatrixOperations
from test.TestUtils import TestUtils


class BoundaryTests(unittest.TestCase):
    def setUp(self):
        """Set up test data"""
        self.matrix_a = np.array([[1, 2]])
        self.matrix_b = np.array([[3, 4]])
        self.matrix_operations = MatrixOperations(self.matrix_a, self.matrix_b)


    def test_empty_matrix_multiplication(self):
        """Test system with empty matrices"""
        matrix_empty = np.array([[]])
        self.matrix_operations.matrix_a = matrix_empty
        self.matrix_operations.matrix_b = matrix_empty
        test_obj = TestUtils()
        try:
            self.matrix_operations.matrix_multiplication()
            test_obj.yakshaAssert("TestEmptyMatrixMultiplication", False, "boundary")
            print("TestEmptyMatrixMultiplication = Failed")
        except ValueError:
            test_obj.yakshaAssert("TestEmptyMatrixMultiplication", True, "boundary")
            print("TestEmptyMatrixMultiplication = Passed")
