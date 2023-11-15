#!/usr/bin/python3
import random
import sys

CORRECT = 0
INCORRECT = 1
LOWER_CASE = 0
ORIG_CASE = 1
TEXT = "text"
CHOICE = "choice"

random.seed(int(sys.argv[-1]))

module_name = sys.argv[1]
test_type = sys.argv[2]
test_sub_type = sys.argv[3]

questions = []
answers = []
with open("questions.txt") as f:
    for line in f:
        question_answer = line.strip().split("|")
        questions.append(question_answer[0])
        answers.append(question_answer[1])

random_answers = []
with open("random_answers.txt") as f:
    for line in f:
        answer = line.strip()
        random_answers.append(answer)


def random_question_num():
    return random.randint(0, len(questions) - 1)


def random_answer():
    return random.choice(answers)


def generate_question():
    print(test_type)
    question_num = random_question_num()
    print(questions[question_num])
    print(answers[question_num])

    if test_type == "check_answer":
        gen_question_check_answer(question_num)


def gen_question_check_answer(question_num):
    lower_original = random.choice([LOWER_CASE, ORIG_CASE])
    correct_incorrect = random.choices([CORRECT, INCORRECT], [0.7, 0.3])[0]
    if correct_incorrect == CORRECT:
        if lower_original == LOWER_CASE:
            print(answers[question_num])
        else:
            print(answers[question_num].lower())
    else:
        if lower_original == LOWER_CASE:
            print(random_answer().lower())
        else:
            print(random_answer())


def generate_choice_question():
    print(test_type)
    question_num = random_question_num()
    print(questions[question_num])

    if test_type == "add_choice":
        gen_choice_question_add_choices(question_num)
    elif test_type == "get_question":
        gen_choice_question_add_choices(question_num)
    elif test_type == "check_answer":
        correct_answer_num = gen_choice_question_add_choices(question_num)
        gen_choice_question_check_answer(correct_answer_num)


def gen_choice_question_add_choices(question_num):
    correct_answer = answers[question_num]
    num_choices = random.randint(2, 4)
    correct_answer_num = random.randint(1, num_choices)
    print(num_choices)

    for i in range(1, num_choices + 1):
        if correct_answer_num == i:
            print(correct_answer)
            print(True)
        else:
            answer = random.choice(random_answers)
            print(answer)
            print(False)

    return correct_answer_num


def gen_choice_question_check_answer(correct_answer_num):
    correct_incorrect = random.choices([CORRECT, INCORRECT], [0.7, 0.3])[0]
    if correct_incorrect == CORRECT:
        print(correct_answer_num)
    else:
        print(correct_answer_num + 1)


def gen_exam_add_text_question():
    question_num = random_question_num()
    print(questions[question_num])
    print(answers[question_num])

    return question_num


def gen_exam_add_choice_question():
    question_num = random_question_num()
    print(questions[question_num])

    correct_ans_num = gen_choice_question_add_choices(question_num)
    return correct_ans_num


def gen_exam_both_types():
    num_questions = random.randint(1, 4)
    print(num_questions)

    for _ in range(num_questions):
        test_sub_type = random.choice([TEXT, CHOICE])
        print(test_sub_type)

        if test_sub_type == TEXT:
            gen_exam_add_text_question()
        else:
            gen_exam_add_choice_question()


def gen_exam_take():
    answer_list = []
    num_questions = random.randint(1, 4)
    print(num_questions)
    # First generate data for creating question instances
    for i in range(num_questions):
        correct_incorrect = random.choice([CORRECT, INCORRECT])
        test_sub_type = random.choice([TEXT, CHOICE])
        print(test_sub_type)

        if test_sub_type == TEXT:
            question_num = gen_exam_add_text_question()
            if correct_incorrect == CORRECT:
                answer_list.append(answers[question_num])
            else:
                answer_list.append(random_answer())
        else:
            correct_ans_num = gen_exam_add_choice_question()
            if correct_incorrect == CORRECT:
                answer_list.append(correct_ans_num)
            else:
                answer_list.append(correct_ans_num + 1)

    # Then generate the answers
    for i in range(num_questions):
        print(answer_list[i])


def generate_exam():
    print(test_type)

    if test_type == "add_question":
        print(test_sub_type)
        if test_sub_type == TEXT:
            gen_exam_add_text_question()
        elif test_sub_type == CHOICE:
            gen_exam_add_choice_question()
    elif test_type == "__str__":
        gen_exam_both_types()
    elif test_type == "take":
        gen_exam_take()


# Main
print(module_name)
if module_name == "question":
    generate_question()
elif module_name == "choicequestion":
    generate_choice_question()
elif module_name == "exam":
    generate_exam()
else:
    assert False, "Invalid module name"
