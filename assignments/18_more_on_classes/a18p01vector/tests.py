import unittest

from vector import Vector


class VectorStringUnitTests(unittest.TestCase):
    """
    Test case 1 (1. String conversion):
    Points: 3
    """

    def test_string_conversion(self):
        # Arrange
        expected = "[[ 12 3 4 ]]"

        # Act
        v = Vector(12, 3, 4)
        actual = str(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class VectorConstructorUnitTests(unittest.TestCase):
    """
    Test case 2 (1.0. Constructor default arguments):
    Points: 1
    """

    def test_constructor_all_defaults(self):
        # Arrange
        expected = "[[ 0 0 0 ]]"

        # Act
        v = Vector()
        actual = str(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_constructor_2_defaults(self):
        # Arrange
        expected = "[[ 5 0 0 ]]"

        # Act
        v = Vector(5)
        actual = str(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_constructor_1_default(self):
        # Arrange
        expected = "[[ 5 -8 0 ]]"

        # Act
        v = Vector(5, -8)
        actual = str(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class VectorLengthUnitTests(unittest.TestCase):
    """
    Test case 3 (2. Length):
    Points: 5
    """

    def test_length_parallel_to_axis(self):
        # Arrange
        expected = 2.0

        # Act
        v = Vector(0, 2)  # [0, 2, 0]
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_unit_parallel_to_axis(self):
        # Arrange
        expected = 1.0

        # Act
        v = Vector(0, 0, 1)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_3_4_5(self):
        # Arrange
        expected = 5.0

        # Act
        v = Vector(3, 4)  # [3, 4, 0]
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_5_12_13(self):
        # Arrange
        expected = 13.0

        # Act
        v = Vector(5, 0, 12)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_8_15_17(self):
        # Arrange
        expected = 17.0

        # Act
        v = Vector(0, 15, 8)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_3_4_5_and_5_12_13(self):
        # Arrange
        expected = 13.0

        # Act
        v = Vector(3, 4, 12)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_3_4_5_and_5_12_13_different_order(self):
        # Arrange
        expected = 13.0

        # Act
        v = Vector(12, 3, 4)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_9_12_15_and_15_8_17(self):
        # Arrange
        expected = 17.0

        # Act
        v = Vector(12, 8, 9)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_9_12_15_and_15_8_17_negative(self):
        # Arrange
        expected = 17.0

        # Act
        v = Vector(12, 8, -9)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_1_2_2_3(self):
        # Arrange
        expected = 3.0

        # Act
        v = Vector(1, 2, 2)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_2_3_6_7(self):
        # Arrange
        expected = 7.0

        # Act
        v = Vector(2, 3, 6)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_length_non_pythagorean_quadruple(self):
        # Arrange
        expected = 3.7416573867739413

        # Act
        v = Vector(1, 2, 3)
        actual = abs(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertAlmostEqual(expected, actual, msg=message)

    def test_vector_not_modified(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = "[[ 12 3 4 ]]"

        # Act
        abs(v)
        actual = str(v)

        # Assert
        message = f"\n\nVector is supposed to remain unchanged as:\n{expected}"
        message += (
            f"\n\nBut you seem to have modified the vector when calculating its length."
        )
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorSumUnitTests(unittest.TestCase):
    """
    Test case 4 (3. Sum):
    Points: 3
    """

    def test_return_type(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = Vector

        # Act
        w = u + v
        actual = type(w)

        # Assert
        message = f"\n\nExpected output type:\n{expected}"
        message += f"\n\nActual output type:\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_sum(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = "[[ 12 13 -10 ]]"

        # Act
        w = u + v
        actual = str(w)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_another_sum(self):
        # Arrange
        u = Vector(-5, 3, 404)
        v = Vector(5, -3, 96)
        expected = "[[ 0 0 500 ]]"

        # Act
        w = u + v
        actual = str(w)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = "[[ 12 3 4 ]]"

        # Act
        w = u + v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = "[[ 0 10 -14 ]]"

        # Act
        w = u + v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when adding the two."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorDifferenceUnitTests(unittest.TestCase):
    """
    Test case 5 (4. Difference):
    Points: 3
    """

    def test_return_type(self):
        # Arrange
        expected = Vector

        # Act
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        w = u - v
        actual = type(w)

        # Assert
        message = f"\n\nExpected output type:\n{expected}"
        message += f"\n\nActual output type:\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_difference(self):
        # Arrange
        expected = "[[ 12 -7 18 ]]"

        # Act
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        w = u - v
        actual = str(w)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_another_difference(self):
        # Arrange
        expected = "[[ -10 6 308 ]]"

        # Act
        u = Vector(-5, 3, 404)
        v = Vector(5, -3, 96)
        w = u - v
        actual = str(w)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = "[[ 12 3 4 ]]"

        # Act
        w = u - v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += (
            f"\n\nBut you seem to have modified the vector when subtracting the two."
        )
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        expected = "[[ 0 10 -14 ]]"

        # Act
        w = u - v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += (
            f"\n\nBut you seem to have modified the vector when subtracting the two."
        )
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorEqualityUnitTests(unittest.TestCase):
    """
    Test case 6 (5. Equality):
    Points: 1
    """

    def test_equality(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(12, 3, 4)

        # Act
        actual = u == v

        # Assert
        self.assertTrue(actual)
        self.assertEqual(u, v)

    def test_identity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = u

        # Act
        actual = u == v

        # Assert
        self.assertTrue(actual)
        self.assertEqual(u, v)

    def test_not_equal(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(12, 4, 3)

        # Act
        actual = u == v

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(u, v)

    def test_another_unequal_pair(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, 3)

        # Act
        actual = u == v

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(u, v)

    def test_another_unequal_pair_with_negatives(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(-12, -3, 4)

        # Act
        actual = u == v

        # Assert
        self.assertFalse(actual)
        self.assertNotEqual(u, v)


class VectorAlmostEqualityUnitTests(unittest.TestCase):
    """
    Test case 7 (5.1 Almost Equal):
    Points: 2
    """

    def test_almost_equal(self):
        # Arrange
        u = Vector(1.2 - 1.0, 3, 4)
        v = Vector(0.2, 3, 4)

        # Act
        actual = u == v

        # Assert
        self.assertTrue(actual)
        self.assertEqual(u, v)

    def test_almost_equal_with_defaults(self):
        # Arrange
        u = Vector(1.2 - 1.0)
        v = Vector(0.2)

        # Act
        actual = u == v

        # Assert
        self.assertTrue(actual)
        self.assertEqual(u, v)

    def test_almost_equal_in_more_dimensions(self):
        # Arrange
        u = Vector(0.3 - 0.1, 0.3 - 0.2, 0.2)
        v = Vector(0.2, 0.1, 1.2 - 1.0)

        # Act
        actual = u == v

        # Assert
        self.assertTrue(actual)
        self.assertEqual(u, v)

    def test_addition(self):
        # Arrange
        u = Vector(0.1, 0.2, 1.1)
        v = Vector(0.2, 0.1, 0.3)
        expected = Vector(0.3, 0.3, 1.4)

        # Act
        actual = u + v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_subtraction(self):
        # Arrange
        u = Vector(0.3, 0.3, 1.2)
        v = Vector(0.2, 0.1, 1.0)
        expected = Vector(0.1, 0.2, 0.2)

        # Act
        actual = u - v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class VectorAdditionIdentitiesUnitTests(unittest.TestCase):
    """
    Test case 8 (5.2 Some identities):
    Points: 2
    """

    def test_default_vector(self):
        # Arrange
        expected = Vector(0, 0, 0)

        # Act
        actual = Vector()

        # Assert
        self.assertEqual(expected, actual)

    def test_neutrality_of_zero_vector(self):
        # Arrange
        O = Vector()
        v = Vector(12, 3, 4)

        # Assert
        self.assertEqual(v + O, v)
        self.assertEqual(O + v, v)

    def test_commutativity_of_addition(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)

        # Assert
        self.assertEqual(u + v, v + u)

    def test_associativity_of_addition(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(0, 10, -14)
        w = Vector(3, 7, 10)

        # Assert
        self.assertEqual((u + v) + w, u + (v + w))


class VectorRightScalingUnitTests(unittest.TestCase):
    """
    Test case 9 (6a. Scaling on right side):
    Points: 3
    """

    def test_scaling(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector(60, 15, 20)

        # Act
        actual = v * 5

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_scaling_by_0(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector()

        # Act
        actual = v * 0

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_scaling_by_1(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = v

        # Act
        actual = v * 1

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_reversing(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector(-12, -3, -4)

        # Act
        actual = v * -1

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_vector_not_modified(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = "[[ 12 3 4 ]]"

        # Act
        w = v * 5
        actual = str(v)

        # Assert
        message = f"\n\nVector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when scaling."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorLeftScalingUnitTests(unittest.TestCase):
    """
    Test case 10 (6b. Scaling on left side):
    Points: 3
    """

    def test_scaling(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector(60, 15, 20)

        # Act
        actual = 5 * v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_scaling_by_0(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector()

        # Act
        actual = 0 * v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_scaling_by_1(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = v

        # Act
        actual = 1 * v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_reversing(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector(-12, -3, -4)

        # Act
        actual = -1 * v

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_vector_not_modified(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = "[[ 12 3 4 ]]"

        # Act
        w = 5 * v
        actual = str(v)

        # Assert
        message = f"\n\nVector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector when scaling."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorScalingIdentitiesUnitTests(unittest.TestCase):
    """
    Test case 11 (6c. Some more identities):
    Points: 2
    """

    def test_domination_of_zero_vector(self):
        # Arrange
        O = Vector()

        # Assert
        self.assertEqual(O * 1, O)
        self.assertEqual(1 * O, O)
        self.assertEqual(O * 5, O)
        self.assertEqual(5 * O, O)

    def test_domination_of_zero(self):
        # Arrange
        O = Vector()
        v = Vector(12, 3, 4)

        # Assert
        self.assertEqual(v * 0, O)
        self.assertEqual(0 * v, O)

    def test_neutrality_of_1(self):
        # Arrange
        v = Vector(12, 3, 4)

        # Assert
        self.assertEqual(v * 1, v)
        self.assertEqual(1 * v, v)

    def test_commutativity_of_scaling(self):
        # Arrange
        v = Vector(12, 3, 4)
        c = 5

        # Assert
        self.assertEqual(c * v, v * c)

    def test_associativity_of_scaling(self):
        # Arrange
        v = Vector(12, 3, 4)
        a = 3
        b = -4

        # Assert
        self.assertEqual((a * b) * v, a * (b * v))

    def test_distributivity(self):
        # Arrange
        u = Vector(1, 2, 3)
        v = Vector(12, 3, 4)
        a = 3
        b = -4

        # Assert
        self.assertEqual(a * (u + v), a * u + a * v)
        self.assertEqual((a + b) * v, a * v + b * v)


class VectorRepresentationUnitTests(unittest.TestCase):
    """
    Test case 12 (7. Representation):
    Points: 4
    """

    def test_representation(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = "Vector(12, 3, 4)"

        # Act
        actual = repr(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_evaluation_of_representation(self):
        # Arrange
        v = Vector(12, 3, 4)
        expected = Vector(12, 3, 4)

        # Act
        actual = eval(repr(v))

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
        self.assertEqual(Vector, type(actual))


class VectorGreaterUnitTests(unittest.TestCase):
    """
    Test case 13 (8a. Greater than):
    Points: 2
    """

    def test_greater(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertTrue(u > v)
        self.assertGreater(u, v)

    def test_not_greater(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertFalse(v > u)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 12 3 4 ]]"

        # Act
        u > v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 3 4 5 ]]"

        # Act
        u > v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorGreaterEqualUnitTests(unittest.TestCase):
    """
    Test case 14 (8b. Greater than or equal):
    Points: 2
    """

    def test_greater(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertTrue(u >= v)
        self.assertGreaterEqual(u, v)

    def test_not_greater_or_equal(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertFalse(v >= u)

    def test_equal(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 12)

        # Assert
        self.assertTrue(u >= v)
        self.assertGreaterEqual(u, v)
        self.assertTrue(v >= u)
        self.assertGreaterEqual(v, u)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 12 3 4 ]]"

        # Act
        u >= v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 3 4 5 ]]"

        # Act
        u >= v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorLessUnitTests(unittest.TestCase):
    """
    Test case 15 (8c. Less than):
    Points: 2
    """

    def test_less(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertTrue(v < u)
        self.assertLess(v, u)

    def test_not_less(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertFalse(u < v)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 12 3 4 ]]"

        # Act
        u < v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 3 4 5 ]]"

        # Act
        u < v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorLessEqualUnitTests(unittest.TestCase):
    """
    Test case 16 (8d. Less than or equal):
    Points: 2
    """

    def test_less(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertTrue(v <= u)
        self.assertLessEqual(v, u)

    def test_not_less_or_equal(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)

        # Assert
        self.assertFalse(u <= v)

    def test_equal(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 12)

        # Assert
        self.assertTrue(u <= v)
        self.assertLessEqual(u, v)
        self.assertTrue(v <= u)
        self.assertLessEqual(v, u)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 12 3 4 ]]"

        # Act
        u <= v
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(3, 4, 5)
        expected = "[[ 3 4 5 ]]"

        # Act
        u <= v
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorDotProductUnitTests(unittest.TestCase):
    """
    Test case 17 (9a. Dot product):
    Points: 5
    """

    def test_dot_product(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        expected = 6

        # Act
        actual = u.dot(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_dot_product_perpendicular(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 0, -3)
        expected = 0

        # Act
        actual = u.dot(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_commutativity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)

        # Assert
        self.assertEqual(u.dot(v), v.dot(u))

    def test_distributivity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        w = Vector(3, 4, 5)

        # Assert
        self.assertEqual(u.dot(v + w), u.dot(v) + u.dot(w))
        self.assertEqual((u + v).dot(w), u.dot(w) + v.dot(w))

    def test_associativity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        c = 5

        # Assert
        self.assertEqual((c * u).dot(v), c * u.dot(v))
        self.assertEqual(u.dot(v * c), u.dot(v) * c)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        expected = "[[ 12 3 4 ]]"

        # Act
        u.dot(v)
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        expected = "[[ 1 2 -3 ]]"

        # Act
        u.dot(v)
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


class VectorCrossProductUnitTests(unittest.TestCase):
    """
    Test case 18 (9b. Cross product):
    Points: 5
    """

    def test_cross_product(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, 3)
        expected = Vector(1, -32, 21)

        # Act
        actual = u.cross(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_dot_product_perpendicular(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 0, -3)
        expected = Vector(-9, 40, -3)

        # Act
        actual = u.cross(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_dot_product_parallel(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(-24, -6, -8)
        O = Vector()
        expected = O

        # Act
        actual = u.cross(v)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_anti_commutativity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)

        # Assert
        self.assertNotEqual(u.cross(v), v.cross(u))
        self.assertEqual(-1 * u.cross(v), v.cross(u))

    def test_distributivity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        w = Vector(3, 4, 5)

        # Assert
        self.assertEqual(u.cross(v + w), u.cross(v) + u.cross(w))
        self.assertEqual((u + v).cross(w), u.cross(w) + v.cross(w))

    def test_associativity(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        c = 5

        # Assert
        self.assertEqual((c * u).cross(v), c * u.cross(v))
        self.assertEqual(u.cross(v * c), u.cross(v) * c)

    def test_left_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        expected = "[[ 12 3 4 ]]"

        # Act
        u.cross(v)
        actual = str(u)

        # Assert
        message = f"\n\nFirst vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)

    def test_right_vector_not_modified(self):
        # Arrange
        u = Vector(12, 3, 4)
        v = Vector(1, 2, -3)
        expected = "[[ 1 2 -3 ]]"

        # Act
        u.cross(v)
        actual = str(v)

        # Assert
        message = f"\n\nSecond vector is supposed to remain unchanged as:\n{expected}"
        message += f"\n\nBut you seem to have modified the vector."
        message += f"\nNow it has been changed to:\n{actual}"
        self.assertEqual(expected, actual, msg=message)


"""
class TemplateUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_template(self):
        # Arrange
        test_input = ""
        expected = True

        # Act
        actual = Vector(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
"""

if __name__ == "__main__":
    unittest.main()
