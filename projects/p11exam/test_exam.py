from question import Question
from choice_question import ChoiceQuestion
from exam import Exam


def main():
    q1 = Question("Who is the inventor of Python?", "Guido van Rossum")

    q2 = ChoiceQuestion("In what year was the Python language first released?")
    q2.add_choice("1991", True)
    q2.add_choice("1995", False)
    q2.add_choice("1998", False)
    q2.add_choice("2000", False)

    q3 = Question("What does OOP stand for?", "Object-oriented programming")

    q4 = ChoiceQuestion("Which of the following is a built-in type in Pyhon?")
    q4.add_choice("array", False)
    q4.add_choice("record", False)
    q4.add_choice("dict", True)

    exam = Exam()
    exam.add_question(q1)
    exam.add_question(q2)
    exam.add_question(q3)
    exam.add_question(q4)

    exam.take()
    print(
        f"Your score is {exam.get_points()} point(s) out of {exam.get_num_questions()}"
    )

    print(exam)


if __name__ == "__main__":
    main()
