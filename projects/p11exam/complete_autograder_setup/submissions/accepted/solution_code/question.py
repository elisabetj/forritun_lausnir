#!/usr/bin/python3


class Question:
    """A class that models an exam question."""

    def __init__(self, question_str, answer_str):
        """Initializes the instance with the given question and answer."""
        self.__question_str = question_str
        self.set_answer(answer_str)

    def __str__(self):
        """Returns a string representation of the instance."""
        return "Q: {} A: {}".format(self.__question_str, self.__answer_str)

    def get_question(self):
        """Returns the question string."""
        return self.__question_str

    def set_answer(self, answer_str):
        """Sets the answer string"""
        self.__answer_str = answer_str

    def check_answer(self, response):
        """Returns true if the given response is equal to the answer,
        otherwise false.
        """
        return response.lower() == self.__answer_str.lower()
