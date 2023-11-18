import random

from typing import List, Tuple


def main():
    random_seed = int(input())
    game = Mastermind(random_seed)
    game.play()
    while play_again():
        game.play()


def play_again() -> bool:
    return input("Would you like to play again (y/n)?\n").lower() == "y"


class Mastermind:
    COLOR_LETTERS = "rgbypo"

    def __init__(self, random_seed) -> None:
        if random_seed is not None:
            random.seed(random_seed)
        self.__game_count = 0

    def play(self) -> None:
        if self.__game_count == 0:
            self.__show_introduction()
        self.__game_count += 1

        self.__show_start_game_header()
        code = self.__generate_random_code()
        guesses_left = 8
        guess = ""
        while not self.__is_game_over(code, guess, guesses_left):
            guess = self.__ask_for_guess(guesses_left)
            if guess != code:
                self.__show_feedback(guess, code)
                guesses_left -= 1
            else:
                self.__show_victory_message()
        if guesses_left == 0:
            self.__show_defeat_message(code)

    def __show_introduction(self) -> None:
        print("Welcome to Mastermind.")
        print("The codemaker has selected a code.")
        print("The code is a sequence of four colors. It may contain duplicates.")
        print("There are 6 possible colors to choose from:")
        print(" - (r)ed")
        print(" - (g)reen")
        print(" - (b)lue")
        print(" - (y)ellow")
        print(" - (p)urple")
        print(" - (o)range")
        print("It's your job to break the code by making a series of guesses.")
        print(
            "Each guess consists of four letters corresponding to the colors listed above."
        )
        print(
            "Example: to guess red, green, blue and orange, type rgbo and press Enter."
        )
        print()

    def __show_start_game_header(self) -> None:
        print("-------------------    The game starts now    ------------------------")

    def __generate_random_code(self) -> str:
        return "".join(random.choices(self.COLOR_LETTERS, k=4))

    def __is_game_over(self, code: str, guess: str, guesses_left) -> bool:
        return guesses_left == 0 or code == guess

    def __ask_for_guess(self, guesses_left: int) -> str:
        guess = input(f"You have {guesses_left} guesses left:\n").lower().strip()
        if not self.__is_valid_guess(guess):
            print(
                "That's not a valid guess.\nPlease enter four letters from an alphabet of",
                self.COLOR_LETTERS,
            )
            guess = self.__ask_for_guess(guesses_left)
        return guess

    def __is_valid_guess(self, guess: str) -> bool:
        if len(guess) != 4:
            return False
        for letter in guess:
            if letter not in self.COLOR_LETTERS:
                return False
        return True

    def __show_feedback(self, guess: str, code: str) -> None:
        unmatched_in_guess, unmatched_in_code = self.__get_unmatched_elements(
            guess, code
        )
        correct_color_and_position = 4 - len(unmatched_in_code)
        correct_color = 0
        for element in unmatched_in_guess:
            if element in unmatched_in_code:
                correct_color += 1
                unmatched_in_code.remove(element)
        print(
            "{:<60}{:>10}".format(
                "Elements with the correct color and position:",
                correct_color_and_position,
            )
        )
        print(
            "{:<60}{:>10}".format(
                "Elements with the correct color but incorrect position:", correct_color
            )
        )

    def __get_unmatched_elements(
        self, guess: str, code: str
    ) -> Tuple[List[str], List[str]]:
        unmatched_in_guess = []
        unmatched_in_code = []
        for guess_element, code_element in zip(guess, code):
            if guess_element != code_element:
                unmatched_in_guess.append(guess_element)
                unmatched_in_code.append(code_element)
        return unmatched_in_guess, unmatched_in_code

    def __show_victory_message(self) -> None:
        print("Congratulations, you have guessed the code!")

    def __show_defeat_message(self, code: str) -> None:
        print(f"You failed to guess {code}. Game over :(")


if __name__ == "__main__":
    main()
