import unittest

from waterbottle import WaterBottle


EPS = 0.00001


class WaterBottleUnitTests(unittest.TestCase):
    """
    Test case 1 (Constructor):
    """

    def test_max_capacity_default(self):
        # Arrange
        expected = 2

        # Act
        bottle = WaterBottle()
        actual = bottle.max_capacity

        # Assert
        message = f"\n\nExpected capacity ({type(expected)}):\n{expected}"
        message += f"\n\nActual capacity ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_max_capacity(self):
        # Arrange
        test_input = 5
        expected = 5

        # Act
        bottle = WaterBottle(max_capacity=test_input)
        actual = bottle.max_capacity

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected capacity ({type(expected)}):\n{expected}"
        message += f"\n\nActual capacity ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_current_contents(self):
        # Arrange
        test_input = 5
        expected = 0

        # Act
        bottle = WaterBottle(max_capacity=test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected capacity ({type(expected)}):\n{expected}"
        message += f"\n\nActual capacity ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 2 (Fill):
    """

    def test_fill_to_default_capacity(self):
        # Arrange
        bottle = WaterBottle()
        expected = 2

        # Act
        bottle.fill()
        actual = bottle.current_contents

        # Assert
        message = f"\n\nExpected contents ({type(expected)}):\n{expected}"
        message += f"\n\nActual contents ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_fill_to_custom_capacity(self):
        # Arrange
        test_input = 10
        bottle = WaterBottle(max_capacity=test_input)
        expected = test_input

        # Act
        bottle.fill()
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected contents ({type(expected)}):\n{expected}"
        message += f"\n\nActual contents ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_refill_when_already_full(self):
        # Arrange
        test_input = 3
        bottle = WaterBottle(max_capacity=test_input)
        bottle.fill()
        expected = test_input

        # Act
        bottle.fill()
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected contents ({type(expected)}):\n{expected}"
        message += f"\n\nActual contents ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_refill_when_neither_empty_nor_full(self):
        # Arrange
        test_input = 5
        bottle = WaterBottle(max_capacity=test_input)
        bottle.fill()
        bottle.drink(amount=3.5)
        expected = test_input

        # Act
        bottle.fill()
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected contents ({type(expected)}):\n{expected}"
        message += f"\n\nActual contents ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 3 (Drink):
    """

    def test_contents_after_drinking_from_default(self):
        # Arrange
        test_input = 0.3
        bottle = WaterBottle()
        bottle.fill()
        expected = 2 - test_input

        # Act
        bottle.drink(test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_contents_after_drinking_more(self):
        # Arrange
        test_input = 3.7
        size = 5
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        expected = size - test_input

        # Act
        bottle.drink(test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_contents_after_drinking_again(self):
        # Arrange
        test_input = 1.4
        size = 6
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        previously_consumed = 2
        bottle.drink(previously_consumed)
        expected = size - previously_consumed - test_input

        # Act
        bottle.drink(test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_contents_after_attempting_to_spit(self):
        # Arrange
        test_input = -0.1
        size = 3
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        previously_consumed = 2
        bottle.drink(previously_consumed)
        expected = size - previously_consumed
        not_expected = size - previously_consumed - test_input

        # Act
        bottle.drink(test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)
        self.assertFalse(abs(not_expected - actual) < EPS, message)

    def test_contents_after_drinking_excessively(self):
        # Arrange
        test_input = 1.2
        size = 3
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        previously_consumed = 2
        bottle.drink(previously_consumed)
        expected = 0
        not_expected = size - previously_consumed - test_input

        # Act
        bottle.drink(test_input)
        actual = bottle.current_contents

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)
        self.assertFalse(abs(not_expected - actual) < EPS, message)

    """
    Test case 4 (Receive):
    """

    def test_drink_from_default(self):
        # Arrange
        bottle = WaterBottle()
        bottle.fill()

        test_input = 0.3
        expected = test_input

        # Act
        actual = bottle.drink(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_drink_more(self):
        # Arrange
        size = 5
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()

        test_input = 3.7
        expected = test_input

        # Act
        actual = bottle.drink(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_drink_again(self):
        # Arrange
        size = 6
        previously_consumed = 2

        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        bottle.drink(previously_consumed)

        test_input = 1.4
        expected = test_input

        # Act
        actual = bottle.drink(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)

    def test_spit(self):
        # Arrange
        size = 5
        previously_consumed = 2

        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        bottle.drink(previously_consumed)

        test_input = -0.1
        expected = 0
        not_expected = test_input

        # Act
        actual = bottle.drink(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)
        self.assertFalse(abs(not_expected - actual) < EPS, message)

    def test_drink_excessively(self):
        # Arrange
        size = 3
        previously_consumed = 2
        remaining = size - previously_consumed

        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        bottle.drink(previously_consumed)

        test_input = 1.2
        expected = remaining
        not_expected = test_input

        # Act
        actual = bottle.drink(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)
        self.assertFalse(abs(not_expected - actual) < EPS, message)

    """
    Test case 5 (Print):
    """

    def test_empty(self):
        # Arrange
        bottle = WaterBottle()
        expected = "The bottle currently holds 0.0L of water."

        # Act
        actual = str(bottle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_full(self):
        # Arrange
        size = 4
        bottle = WaterBottle(max_capacity=size)
        bottle.fill()

        expected = "The bottle currently holds 4.0L of water."

        # Act
        actual = str(bottle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_3_of_5(self):
        # Arrange
        size = 5
        previously_consumed = 2

        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        bottle.drink(previously_consumed)

        expected = "The bottle currently holds 3.0L of water."

        # Act
        actual = str(bottle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_float(self):
        # Arrange
        size = 6
        previously_consumed = 4.3

        bottle = WaterBottle(max_capacity=size)
        bottle.fill()
        bottle.drink(previously_consumed)

        expected = "The bottle currently holds 1.7L of water."

        # Act
        actual = str(bottle)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()


"""
template:


class UnitTestTemplate(unittest.TestCase):
    def test_template(self):
        # Arrange
        test_input = ""
        expected = True

        # Act
        actual = WaterBottle(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertTrue(abs(expected - actual) < EPS, message)
        self.assertEqual(expected, actual, message)
"""
