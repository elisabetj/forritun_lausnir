import unittest

from solution_code import shuffle


class ShuffleUnitTests(unittest.TestCase):

    """
    Test case 1 (Annotations):
    """

    def test_annotations_original_list(self):
        # Arrange
        expected = list

        # Act
        annotations = shuffle.__annotations__

        # Assert
        self.assertTrue(
            "original_list" in annotations,
            "No annotation found for the original_list parameter",
        )
        actual = annotations["original_list"]

        message = f"\n\nChecking annotation type for original_list parameter:"
        message += f"\n\nExpected annotation:\n{expected}"
        message += f"\n\nActual annotation:\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_annotations_start_from_back(self):
        # Arrange
        expected = bool

        # Act
        annotations = shuffle.__annotations__

        # Assert
        self.assertTrue(
            "start_from_back" in annotations,
            "No annotation found for the start_from_back parameter",
        )
        actual = annotations["start_from_back"]

        message = f"\n\nChecking annotation type for start_from_back parameter:"
        message += f"\n\nExpected annotation:\n{expected}"
        message += f"\n\nActual annotation:\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_annotations_return(self):
        # Arrange
        expected = list

        # Act
        annotations = shuffle.__annotations__

        # Assert
        self.assertTrue(
            "return" in annotations,
            "No annotation found for the return value of the shuffle function",
        )
        actual = annotations["return"]

        message = f"\n\nChecking annotation type for return value:"
        message += f"\n\nExpected annotation:\n{expected}"
        message += f"\n\nActual annotation:\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 2 (Empty):
    Description: Empty list.
    """

    def test_empty(self):
        # Arrange
        test_input = []
        expected = []

        # Act
        actual = shuffle(original_list=test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 3 (Even back):
    Description: Even number of elements, starting from the back.
    """

    def test_even_number_start_from_back(self):
        # Arrange
        test_input = [1, 2, 3, 4, 5, 6]
        expected = [6, 1, 5, 2, 4, 3]

        # Act
        actual = shuffle(original_list=test_input, start_from_back=True)

        # Assert
        message = f"\n\nInput:"
        message += f"\noriginal_list = {test_input} ({type(test_input)})"
        message += f"\nstart_from_back = True"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 4 (Even front):
    Description: Even number of elements, starting from beginning.
    """

    def test_even_number_start_from_beginning(self):
        # Arrange
        test_input = [1, 2, 3, 4, 5, 6]
        expected = [1, 6, 2, 5, 3, 4]

        # Act
        actual = shuffle(original_list=test_input)

        # Assert
        message = f"\n\nInput:"
        message += f"\noriginal_list = {test_input} ({type(test_input)})"
        message += f"\nstart_from_back = False (default)"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 5 (Odd back):
    Description: Odd number of elements, starting from the back.
    """

    def test_odd_number_start_from_back(self):
        # Arrange
        test_input = [1, 2, 3, 4, 5]
        expected = [5, 1, 4, 2, 3]

        # Act
        actual = shuffle(original_list=test_input, start_from_back=True)

        # Assert
        message = f"\n\nInput:"
        message += f"\noriginal_list = {test_input} ({type(test_input)})"
        message += f"\nstart_from_back = True"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 6 (Odd front):
    Description: Odd number of elements, starting from beginning.
    """

    def test_odd_number_start_from_beginning(self):
        # Arrange
        test_input = [1, 2, 3, 4, 5]
        expected = [1, 5, 2, 4, 3]

        # Act
        actual = shuffle(original_list=test_input)

        # Assert
        message = f"\n\nInput:"
        message += f"\noriginal_list = {test_input} ({type(test_input)})"
        message += f"\nstart_from_back = False (default)"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    """
    Test case 7 (Original unchanged):
    Description: Don't mess with the original.
    """

    def test_original_unchanged(self):
        # Arrange
        test_input = ["a", "b", "c", "d"]
        copy_of_original = test_input[:]
        expected = copy_of_original

        # Act
        shuffle(test_input)
        actual = test_input

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nOriginal list expected to remain unchanged as ({type(expected)}):\n{expected}"
        message += f"\n\nActual state of original list after calling the function, ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
