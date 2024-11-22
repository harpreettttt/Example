# test_vector2d.py

import unittest
from vector2d import Vector2D

class TestVector2D(unittest.TestCase):
    def setUp(self):
        """
        Set up Vector2D instances for testing.
        This method is called before each test.
        """
        self.v1 = Vector2D(3.0, 4.0)
        self.v2 = Vector2D(1.0, 2.0)
        self.zero_vector = Vector2D(0.0, 0.0)

    def test_initialization(self):
        """
        Test that Vector2D objects are initialized correctly.
        """
        self.assertEqual(self.v1.x, 3.0)
        self.assertEqual(self.v1.y, 4.0)
        self.assertEqual(self.v2.x, 1.0)
        self.assertEqual(self.v2.y, 2.0)
        self.assertEqual(self.zero_vector.x, 0.0)
        self.assertEqual(self.zero_vector.y, 0.0)

    def test_addition(self):
        """
        Test vector addition using the + operator.
        """
        result = self.v1 + self.v2
        expected = Vector2D(4.0, 6.0)
        self.assertEqual(result, expected)

    def test_addition_type_error(self):
        """
        Test that adding a non-Vector2D instance raises a TypeError.
        """
        with self.assertRaises(TypeError):
            _ = self.v1 + "not a vector"

    def test_subtraction(self):
        """
        Test vector subtraction using the - operator.
        """
        result = self.v1 - self.v2
        expected = Vector2D(2.0, 2.0)
        self.assertEqual(result, expected)

    def test_subtraction_type_error(self):
        """
        Test that subtracting a non-Vector2D instance raises a TypeError.
        """
        with self.assertRaises(TypeError):
            _ = self.v1 - 5

    def test_scalar_multiplication_left(self):
        """
        Test scalar multiplication using the * operator (vector * scalar).
        """
        scalar = 2.0
        result = self.v1 * scalar
        expected = Vector2D(6.0, 8.0)
        self.assertEqual(result, expected)

    def test_scalar_multiplication_right(self):
        """
        Test scalar multiplication using the * operator (scalar * vector).
        """
        scalar = 3.0
        result = scalar * self.v2
        expected = Vector2D(3.0, 6.0)
        self.assertEqual(result, expected)

    def test_scalar_multiplication_type_error(self):
        """
        Test that multiplying by a non-numeric type raises a TypeError.
        """
        with self.assertRaises(TypeError):
            _ = self.v1 * "invalid scalar"
        with self.assertRaises(TypeError):
            _ = "invalid scalar" * self.v1

    def test_repr(self):
        """
        Test the __repr__ method for correct string representation.
        """
        expected_repr = "Vector2D(3.0, 4.0)"
        self.assertEqual(repr(self.v1), expected_repr)

    def test_equality(self):
        """
        Test the __eq__ method for comparing two Vector2D instances.
        """
        another_v1 = Vector2D(3.0, 4.0)
        different_v = Vector2D(5.0, 6.0)
        self.assertEqual(self.v1, another_v1)
        self.assertNotEqual(self.v1, self.v2)
        self.assertNotEqual(self.v1, different_v)
        self.assertNotEqual(self.v1, "not a vector")

    def test_zero_vector_operations(self):
        """
        Test operations involving the zero vector.
        """
        # Addition with zero vector
        result = self.v1 + self.zero_vector
        self.assertEqual(result, self.v1)

        # Subtraction with zero vector
        result = self.v1 - self.zero_vector
        self.assertEqual(result, self.v1)

        # Scalar multiplication with zero
        result = self.v1 * 0
        expected = self.zero_vector
        self.assertEqual(result, expected)

    def test_negative_scalars(self):
        """
        Test scalar multiplication with negative values.
        """
        scalar = -1.5
        result = self.v2 * scalar
        expected = Vector2D(-1.5, -3.0)
        self.assertEqual(result, expected)

    def test_floating_point_precision(self):
        """
        Test operations with floating-point precision.
        """
        v_a = Vector2D(0.1, 0.2)
        v_b = Vector2D(0.2, 0.3)
        result = v_a + v_b
        expected = Vector2D(0.3, 0.5)
        self.assertAlmostEqual(result.x, expected.x)
        self.assertAlmostEqual(result.y, expected.y)

if __name__ == '__main__':
    unittest.main()