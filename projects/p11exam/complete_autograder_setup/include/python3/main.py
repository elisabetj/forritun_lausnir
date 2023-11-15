#!/usr/bin/python3

import sys
import importlib
from typing import Iterable

TEXT = "text"
CHOICE = "choice"

sys.dont_write_bytecode = True


def main():
    module_name = input()
    if module_name == "question":
        test_question()
    elif module_name == "choicequestion":
        test_choice_question()
    elif module_name == "exam":
        test_exam()
    else:
        assert False, "Unknown test type"


def test_question():
    callables = prepare_question()

    callable_name = input()
    callables[callable_name]()


def test_choice_question():
    callables = prepare_choice_question()

    callable_name = input()
    callables[callable_name]()


def test_exam():
    callables = prepare_exam()

    callable_name = input()
    callables[callable_name]()


def prepare_exam():
    module_name = "exam"
    class_name = "Exam"
    callables = {
        "__init__": test_exam_init,
        "__str__": test_exam_str,
        "add_question": test_exam_add_question,
        "take": test_exam_take,
    }

    prepare_question()
    prepare_choice_question()

    if not prepare(module_name, class_name, callables):
        return

    return callables


def prepare_choice_question():
    module_name = "choice_question"
    class_name = "ChoiceQuestion"
    callables = {
        "__init__": test_choice_question_init,
        "__str__": test_choice_question_str,
        "add_choice": test_choice_question_add,
        "get_question": test_choice_question_get_question,
        "check_answer": test_choice_question_check_answer,
    }

    prepare_question()

    if not prepare(module_name, class_name, callables):
        return

    return callables


def prepare_question():
    module_name = "question"
    class_name = "Question"
    callables = {
        "__init__": test_question_init,
        "__str__": test_question_str,
        "get_question": test_question_get_question,
        "check_answer": test_question_check_answer,
    }

    if not prepare(module_name, class_name, callables):
        return

    return callables


def prepare(module_name: str, class_name: str, expected_callables: Iterable):
    try:
        module = importlib.import_module(module_name)
    except ImportError:
        print(f"Could not import module {module_name}, does {module_name}.py exist?")
        return False

    if not hasattr(module, class_name):
        print(f"Could not find class {class_name} in module {module_name}")
        return False

    cls = getattr(module, class_name)

    # for callable_name in expected_callables:
    #    if not hasattr(cls, callable_name):
    #        print(f"Could not find member function {callable_name} of class {class_name}")
    #        return False

    globals()[module_name] = module
    globals()[class_name] = cls
    return True


def test_question_init():
    question = input()
    answer = input()
    instance = None
    try:
        instance = Question(question, answer)
        # Check for the existance of specific private variables
        instance._Question__question_str
        instance._Question__answer_str
    except Exception as e:
        print(f"Error calling Question constructor: {e}")
    return instance


def test_question_str():
    instance = test_question_init()
    if instance is not None:
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing question: {e}")
    return instance


def test_question_get_question():
    instance = test_question_init()
    if instance is not None:
        try:
            print(instance.get_question())
        except Exception as e:
            print(f"Error calling get_question for question: {e}")
    return instance


def test_question_check_answer():
    instance = test_question_init()
    if instance is not None:
        try:
            guess = input()
            print(instance.check_answer(guess))
        except Exception as e:
            print(f"Error calling check_answer for question: {e}")
    return instance


def test_choice_question_init():
    question = input()
    instance = None
    try:
        instance = ChoiceQuestion(question)
    except Exception as e:
        print(f"Error calling ChoiceQuestion constructor: {e}")

    if not isinstance(instance, Question):
        raise TypeError("ChoiceQuestion should be a subclass of Question")

    return instance


def test_choice_question_str():
    instance = test_choice_question_init()
    if instance is not None:
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing choice question: {e}")
    return instance


def test_choice_question_add_choices(instance):
    toBool = {"True": True, "False": False}

    num_choices = int(input())
    try:
        for i in range(num_choices):
            choice_str = input()
            true_false_str = input()
            true_or_false = toBool[true_false_str]
            instance.add_choice(choice_str, true_or_false)
    except Exception as e:
        print(f"Error calling add_choice for choice question: {e}")


def test_choice_question_add():
    instance = test_choice_question_init()
    if instance is not None:
        test_choice_question_add_choices(instance)
        try:
            print(instance)
        except Exception as e:
            print(f"Error printing choice question: {e}")
    return instance


def test_choice_question_get_question():
    instance = test_choice_question_init()
    if instance is not None:
        test_choice_question_add_choices(instance)
        try:
            print(instance.get_question())
        except Exception as e:
            print(f"Error getting choice question: {e}")

    return instance


def test_choice_question_check_answer():
    instance = test_choice_question_init()
    if instance is not None:
        test_choice_question_add_choices(instance)
        answer_choice = input()
        try:
            true_or_false = instance.check_answer(answer_choice)
            print(true_or_false)
        except Exception as e:
            print(f"Error calling check_answer for choice question: {e}")

    return instance


def test_exam_init():
    instance = None
    try:
        instance = Exam()
    except Exception as e:
        print(f"Error calling Exam constructor: {e}")
    return instance


def test_exam_add_question():
    question_type = input()
    if question_type == TEXT:
        test_exam_add_text_question()
    elif question_type == CHOICE:
        test_exam_add_choice_question()
    else:
        print("Unknown question type")


def test_exam_add_text_question(exam=None):
    question = test_question_init()

    if exam is None:
        exam = test_exam_init()
    try:
        exam.add_question(question)
    except Exception as e:
        print(f"Error adding an instance of Question to an instance of Exam: {e}")
    return exam


def test_exam_add_choice_question(exam=None):
    question = test_choice_question_init()
    test_choice_question_add_choices(question)

    if exam is None:
        exam = test_exam_init()
    try:
        exam.add_question(question)
    except Exception as e:
        print(f"Error adding an instance of ChoiceQuestion to an instance of Exam: {e}")
    return exam


def test_exam_str():
    exam = test_exam_init()
    try:
        print(exam)
    except Exception as e:
        print(f"Error printing exam: {e}")

    num_questions = int(input())
    for _ in range(num_questions):
        question_type = input()
        if question_type == TEXT:
            test_exam_add_text_question(exam)
        elif question_type == CHOICE:
            test_exam_add_choice_question(exam)

    try:
        print(exam)
    except Exception as e:
        print(f"Error printing exam: {e}")


def test_exam_take():
    exam = test_exam_init()

    num_questions = int(input())
    for i in range(num_questions):
        test_sub_type = input()
        if test_sub_type == TEXT:
            test_exam_add_text_question(exam)
        elif test_sub_type == CHOICE:
            test_exam_add_choice_question(exam)
    try:
        exam.take()
    except Exception as e:
        print(f"Error taking an Exam: {e}")


if __name__ == "__main__":
    main()
