#!/usr/bin/python3


class Exam:
    """A class that models an exam."""

    def __init__(self):
        """Initializes an instance of an exam."""
        self.__question_list = []
        self.__points = 0

    def __str__(self):
        """Returns a string representation of all questions and answers."""
        str_list = [str(question) for question in self.__question_list]
        questions_str = "\n".join(str_list)

        return questions_str

    def __update_points(self, question, answer):
        """Update the points obtained in the exam."""
        if question.check_answer(answer):
            self.__points += 1

    def __present_question(self, question):
        """Presents the question and allows the user to answer it."""
        print(question.get_question())
        answer = input()
        print(question.check_answer(answer))
        self.__update_points(question, answer)
        print()

    def get_points(self):
        """Returns the points obtained."""
        return self.__points

    def get_num_questions(self):
        """Returns the number of questions."""
        return len(self.__question_list)

    def add_question(self, question):
        """Adds an instance of Question to the exam."""
        self.__question_list.append(question)

    def take(self):
        """Allows the user to take the exam.
        The Question questions are presented first
        and then the ChoiceQuestion questions.
        """
        for question in self.__question_list:
            self.__present_question(question)
