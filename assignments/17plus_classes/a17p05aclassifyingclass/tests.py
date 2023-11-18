import unittest

from solution_code import Sample, ClosestMeanClassifier


MALE = "m"
FEMALE = "f"


class ClassifierUnitTests(unittest.TestCase):
    """
    Unit tests:

    Test case 1:
    Points: 5
    """

    def setUp(self):
        men_heights = [186, 182, 188, 183, 174, 192, 177, 163, 180, 166]
        women_heights = [167, 174, 174, 167, 159, 169, 166, 165, 174, 163]
        men_samples = [Sample(height, MALE) for height in men_heights]
        women_samples = [Sample(height, FEMALE) for height in women_heights]
        samples = men_samples + women_samples
        self.classifier = ClosestMeanClassifier(samples)

    def test_classify_210(self):
        # Arrange
        test_input = 210
        expected = MALE

        # Act
        actual = self.classifier.classify(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_classify_173(self):
        # Arrange
        test_input = 173
        expected = FEMALE

        # Act
        actual = self.classifier.classify(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_classify_174(self):
        # Arrange
        test_input = 174
        expected = MALE

        # Act
        actual = self.classifier.classify(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_classify_154(self):
        # Arrange
        test_input = 154
        expected = FEMALE

        # Act
        actual = self.classifier.classify(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()
