#!/usr/bin/python3

from hangman import Hangman


def main():
    run_problem_statement_example()


def run_problem_statement_example():
    hangword = Hangman("Testing")
    print(hangword)
    print(hangword.guess_letter("i"))
    print(hangword.guess_letter("I"))
    print(hangword.guess_letter("a"))
    hangword.guess_letter("t")
    print(hangword)
    hangword.guess_letter("E")
    hangword.guess_letter("s")
    print(hangword)
    hangword.guess_letter("i")
    hangword.guess_letter("N")
    hangword.guess_letter("g")
    print(hangword)


if __name__ == "__main__":
    main()
