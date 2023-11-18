import unittest

from hangman import Hangman


class HangmanCorrectGuessesUnitTests(unittest.TestCase):
    """
    Test case 1 (1. Correct guesses):
    """

    def test_normal(self):
        # Arrange
        test_input = "Tjónaskýrsla"

        expected_0 = "_ _ _ _ _ _ _ _ _ _ _ _\nNumber of incorrect guesses: 0"
        expected_1 = "T _ _ _ _ _ _ _ _ _ _ _\nNumber of incorrect guesses: 0"
        expected_2 = "T _ _ _ A _ _ _ _ _ _ A\nNumber of incorrect guesses: 0"
        expected_3 = "T _ _ _ A S _ _ _ S _ A\nNumber of incorrect guesses: 0"
        expected_4 = "T J _ _ A S _ _ _ S _ A\nNumber of incorrect guesses: 0"
        expected_5 = "T J _ _ A S _ _ _ S L A\nNumber of incorrect guesses: 0"
        expected_6 = "T J _ N A S _ _ _ S L A\nNumber of incorrect guesses: 0"
        expected_7 = "T J Ó N A S _ _ _ S L A\nNumber of incorrect guesses: 0"
        expected_8 = "T J Ó N A S _ Ý _ S L A\nNumber of incorrect guesses: 0"
        expected_9 = "T J Ó N A S K Ý _ S L A\nNumber of incorrect guesses: 0"
        expected_10 = "T J Ó N A S K Ý R S L A\nNumber of incorrect guesses: 0"

        # Act
        secret = Hangman(test_input)
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_0)}):\n{expected_0}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_0, actual, message)

        # Act
        secret.guess_letter("t")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_1)}):\n{expected_1}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_1, actual, message)

        # Act
        secret.guess_letter("a")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_2)}):\n{expected_2}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_2, actual, message)

        # Act
        secret.guess_letter("s")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_3)}):\n{expected_3}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_3, actual, message)

        # Act
        secret.guess_letter("j")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_4)}):\n{expected_4}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_4, actual, message)

        # Act
        secret.guess_letter("l")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_5)}):\n{expected_5}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_5, actual, message)

        # Act
        secret.guess_letter("n")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_6)}):\n{expected_6}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_6, actual, message)

        # Act
        secret.guess_letter("ó")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_7)}):\n{expected_7}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_7, actual, message)

        # Act
        secret.guess_letter("ý")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_8)}):\n{expected_8}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_8, actual, message)

        # Act
        secret.guess_letter("k")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_9)}):\n{expected_9}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_9, actual, message)

        # Act
        secret.guess_letter("r")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected_10)}):\n{expected_10}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected_10, actual, message)

    def test_guess_letter_return_value(self):
        # Arrange
        test_input = "Tjónaskýrsla"
        secret = Hangman(test_input)

        expected = True

        # Act
        actual = secret.guess_letter("t")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("T")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("t")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("a")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("s")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


class HangmanIncorrectGuessesUnitTests(unittest.TestCase):
    """
    Test case 2 (2. Incorrect guesses):
    """

    def test_miss(self):
        # Arrange
        test_input = "Tjónaskýrsla"
        secret = Hangman(test_input)

        expected = "_ _ _ _ _ _ _ _ _ _ _ _\nNumber of incorrect guesses: 2"

        # Act
        secret.guess_letter("x")
        secret.guess_letter("y")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_interleaved(self):
        # Arrange
        test_input = "Tjónaskýrsla"
        secret = Hangman(test_input)

        expected = "_ _ _ N A S K _ R S _ A\nNumber of incorrect guesses: 3"

        # Act
        secret.guess_letter("e")
        secret.guess_letter("r")
        secret.guess_letter("s")
        secret.guess_letter("a")
        secret.guess_letter("m")
        secret.guess_letter("h")
        secret.guess_letter("n")
        secret.guess_letter("k")
        actual = str(secret)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

    def test_guess_letter_return_value(self):
        # Arrange
        test_input = "Tjónaskýrsla"
        secret = Hangman(test_input)

        expected = False

        # Act
        actual = secret.guess_letter("x")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("y")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("e")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("m")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

        # Act
        actual = secret.guess_letter("h")

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)


if __name__ == "__main__":
    unittest.main()


"""
template:


class CodingRoomsUnitTests(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_template(self):
        # Arrange
        test_input = ""
        expected = True

        # Act
        actual = Hangman(test_input)

        # Assert
        message = f"\n\nInput ({type(test_input)}):\n{test_input}"
        message += f"\n\nExpected output ({type(expected)}):\n{expected}"
        message += f"\n\nActual output ({type(actual)}):\n{actual}"
        self.assertEqual(expected, actual, message)

"""
