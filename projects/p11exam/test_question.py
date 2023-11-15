from question import Question


def main():
    q = Question("Who is the inventor of Python?", "Guido van Rossum")
    answer_question(q)
    print(repr(q))


def answer_question(a_question):
    print(a_question.get_question())
    response = input()
    print(a_question.check_answer(response))


if __name__ == "__main__":
    main()
