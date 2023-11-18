class Hangman:
    def __init__(self, word) -> None:
        self.word = word.upper()
        self.revealed_set = set()
        self.incorrect_guesses = 0

    def guess_letter(self, letter: str) -> bool:
        """Returns wether the guess was correct.

        If the guess was correct, the letter will now no longer be hidden.
        """

        if self._validate_character(letter):
            self._reveal_letter(letter)
            return True
        else:
            self.incorrect_guesses += 1
            return False

    def _validate_character(self, char: str) -> bool:
        """Checks if the input is a single character and that it is found within the word."""

        if len(char) != 1:
            return False
        else:
            return self._char_in_word(char)

    def _char_in_word(self, char: str) -> bool:
        """Checks if the argument character is in the word (case-insensitive)."""

        return char.upper() in self.word

    def _reveal_letter(self, letter: str) -> None:
        """Reveals a letter in the word.

        From now on when the word is printed,
        all occurrences of this letter should be displayed.
        """

        self.revealed_set.add(letter.upper())

    def __str__(self) -> str:
        """Shows the word, only displaying the revealed letters.

        Letters that are still hidden are replaced with "_".
        Letters are printed in uppercase.
        Also shows the number of incorrect guesses.
        """

        return_str = " ".join(
            [char if char in self.revealed_set else "_" for char in self.word]
        )
        return_str += f"\nNumber of incorrect guesses: {self.incorrect_guesses}"

        return return_str
