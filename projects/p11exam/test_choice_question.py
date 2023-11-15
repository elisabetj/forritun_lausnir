from choice_question import ChoiceQuestion


def main():
    q = ChoiceQuestion("In what year was the Python language first released?")
    q.add_choice("1991", True)
    q.add_choice("1995", False)
    q.add_choice("1998", False)
    q.add_choice("2000", False)

    answer_question(q)
    print(q)


def answer_question(a_question):
    print(a_question.get_question())
    response = input()
    print(a_question.check_answer(response))


if __name__ == "__main__":
    main()
