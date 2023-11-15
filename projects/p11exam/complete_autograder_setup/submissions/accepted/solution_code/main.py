#!/usr/bin/python3

import sys
import importlib
from typing import Iterable

from question import Question
from choice_question import ChoiceQuestion
from exam import Exam


TEXT = "text"
CHOICE = "choice"

sys.dont_write_bytecode = True


def main():
    module_name = input()
    if module_name == "question":
        demonstrate_question()
    elif module_name == "choicequestion":
        demonstrate_choice_question()
    elif module_name == "exam":
        demonstrate_exam()
    else:
        assert False, f"Unknown module {module_name}."


def demonstrate_question():
    callables = {
        "__init__": create_question,
        "__str__": print_question,
        "get_question": demonstrate_get_question,
        "check_answer": demonstrate_question_check_answer,
    }

    callable_name = input()
    callables[callable_name]()


def demonstrate_choice_question():
    callables = {
        "__init__": create_choice_question,
        "__str__": print_choice_question,
        "add_choice": demonstrate_adding_answers_to_choice_question,
        "get_question": demonstrate_choice_question_get_question,
        "check_answer": demonstrate_choice_question_check_answer,
    }

    callable_name = input()
    callables[callable_name]()


def demonstrate_exam():
    callables = {
        "__init__": create_exam,
        "__str__": print_exam,
        "add_question": demonstrate_exam_add_question,
        "take": demonstrate_exam_take,
    }

    callable_name = input()
    callables[callable_name]()


def create_question():
    question = input()
    answer = input()
    instance = Question(question, answer)
    return instance


def print_question():
    instance = create_question()
    print(instance)
    return instance


def demonstrate_get_question():
    instance = create_question()
    print(instance.get_question())
    return instance


def demonstrate_question_check_answer():
    instance = create_question()
    guess = input()
    print(instance.check_answer(guess))
    return instance


def create_choice_question():
    question = input()
    instance = ChoiceQuestion(question)
    return instance


def print_choice_question():
    instance = create_choice_question()
    print(instance)
    return instance


def add_choices(instance: ChoiceQuestion):
    toBool = {"True": True, "False": False}

    num_choices = int(input())
    for _ in range(num_choices):
        choice_str = input()
        true_false_str = input()
        true_or_false = toBool[true_false_str]
        instance.add_choice(choice_str, true_or_false)


def demonstrate_adding_answers_to_choice_question():
    instance = create_choice_question()
    add_choices(instance)
    print(instance)
    return instance


def demonstrate_choice_question_get_question():
    instance = create_choice_question()
    add_choices(instance)
    print(instance.get_question())
    return instance


def demonstrate_choice_question_check_answer():
    instance = create_choice_question()
    add_choices(instance)
    answer_choice = input()
    true_or_false = instance.check_answer(answer_choice)
    print(true_or_false)
    return instance


def create_exam():
    instance = Exam()
    return instance


def demonstrate_exam_add_question():
    question_type = input()
    if question_type == TEXT:
        add_text_question()
    elif question_type == CHOICE:
        add_choice_question()
    else:
        print("Unknown question type")


def add_text_question(exam=None):
    question = create_question()

    if exam is None:
        exam = create_exam()

    exam.add_question(question)
    return exam


def add_choice_question(exam=None):
    question = create_choice_question()
    add_choices(question)

    if exam is None:
        exam = create_exam()

    exam.add_question(question)
    return exam


def print_exam():
    exam = create_exam()
    print(exam)

    num_questions = int(input())
    for _ in range(num_questions):
        question_type = input()
        if question_type == TEXT:
            add_text_question(exam)
        elif question_type == CHOICE:
            add_choice_question(exam)

    print(exam)


def demonstrate_exam_take():
    exam = create_exam()

    num_questions = int(input())
    for _ in range(num_questions):
        sub_type = input()
        if sub_type == TEXT:
            add_text_question(exam)
        elif sub_type == CHOICE:
            add_choice_question(exam)

    exam.take()


if __name__ == "__main__":
    main()
