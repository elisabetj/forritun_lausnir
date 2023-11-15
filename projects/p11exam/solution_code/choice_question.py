#!/usr/bin/python3

from question import Question


class ChoiceQuestion(Question):
    """A class that models multiple choice exam question."""

    def __init__(self, question_str):
        """Initializes the instance with empty question and choices."""
        super().__init__(question_str, "")
        self._choices = []

    def get_question(self):
        """Returns the question and the choices as a string."""
        result_str = super().get_question()

        num_choices = len(self._choices)
        for i in range(num_choices):
            choice_no = i + 1
            result_str += f"\n{choice_no}. {self._choices[i]}"

        return result_str

    def add_choice(self, choice, correct):
        """Adds an answer choice to the question.

        correct is True if this is the correct choice, else False.
        """
        self._choices.append(choice)
        if correct:
            answer_str = str(len(self._choices))
            self.set_answer(answer_str)
