"""
I/O tests:

Test case 1:

Input:
1,2,bla,42,52,,0,,t,,,

Output:
(True, True, True, True, True, False, False, False, True, False, False, False)


Test case 2:

Input:
0,,1,10,-1

Output:
(False, False, True, True, True)


Unit tests:

Test case 3:
"""

# assert (
#     type(list_to_bool_tuple([1, 2, 3])) == tuple
# ), "Return type of list_to_bool_tuple is not a tuple."

import unittest

from solution_code import list_to_bool_tuple


class ConversionUnitTests(unittest.TestCase):
    def test_type(self):
        # Arrange
        test_input = [1, 2, 3]
        expected = tuple

        # Act
        actual = list_to_bool_tuple(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected type of output: {expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        message += "\n\nReturn type of list_to_bool_tuple is not a tuple."
        self.assertEqual(expected, type(actual), message)


if __name__ == "__main__":
    unittest.main()
