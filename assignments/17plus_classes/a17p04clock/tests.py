import unittest

from clock import Clock


class TestClockInitialize(unittest.TestCase):
    """
    Test case 1 (1. Initialize):
    Points: 1
    """

    def test_initialize_default(self):
        # Arrange
        expected = "0 hours, 0 minutes and 0 seconds."

        # Act
        clock = Clock()
        actual = str(clock)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_initialize(self):
        # Arrange
        input_hours = 8
        input_minutes = 29
        input_seconds = 59
        expected = "8 hours, 29 minutes and 59 seconds."

        # Act
        clock = Clock(input_hours, input_minutes, input_seconds)
        actual = str(clock)

        # Assert
        message = f"\n\nInput:"
        message += f"\n hours: {input_hours} ({type(input_hours)})"
        message += f"\n minutes: {input_minutes} ({type(input_minutes)})"
        message += f"\n seconds: {input_seconds} ({type(input_seconds)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_initialize_no_seconds(self):
        # Arrange
        input_hours = 8
        input_minutes = 30
        expected = "8 hours, 30 minutes and 0 seconds."

        # Act
        clock = Clock(input_hours, input_minutes)
        actual = str(clock)

        # Assert
        message = f"\n\nInput:"
        message += f"\n hours: {input_hours} ({type(input_hours)})"
        message += f"\n minutes: {input_minutes} ({type(input_minutes)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_initialize_seconds_only(self):
        # Arrange
        input_seconds = 10000
        expected = "2 hours, 46 minutes and 40 seconds."

        # Act
        clock = Clock(seconds=input_seconds)
        actual = str(clock)

        # Assert
        message = f"\n\nInput:"
        message += f"\n seconds: {input_seconds} ({type(input_seconds)})"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class TestClockUpdate(unittest.TestCase):
    """
    Test case 2 (2. Update):
    Points: 1
    """

    def setUp(self):
        self.clock = Clock()

    def test_str_update(self):
        # Arrange
        test_input = "03:21:34"
        expected = "3 hours, 21 minutes and 34 seconds."

        # Act
        self.clock.str_update(test_input)
        actual = str(self.clock)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class TestClockAdd(unittest.TestCase):
    """
    Test case 3 (3. Add):
    Points: 2
    """

    def setUp(self):
        self.clock1 = Clock()
        self.clock2 = Clock()

    def test_add(self):
        # Arrange
        self.clock1.str_update("03:21:34")
        self.clock2.str_update("05:45:52")
        expected = "9 hours, 7 minutes and 26 seconds."

        # Act
        clock = self.clock1.add_clocks(self.clock2)
        actual = str(clock)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_add_with_overflow(self):
        # Arrange
        self.clock1.str_update("20:10:52")
        self.clock2.str_update("08:49:24")
        expected = "5 hours, 0 minutes and 16 seconds."

        # Act
        clock = self.clock1.add_clocks(self.clock2)
        actual = str(clock)

        # Assert
        message = f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


"""
template:

class TestClock(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_template(self):
        # Arrange
        test_input = ""
        expected = "0 hours, 0 minutes and 0 seconds."

        # Act
        clock = Clock(test_input)
        actual = str(clock)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)
"""

if __name__ == "__main__":
    unittest.main()
