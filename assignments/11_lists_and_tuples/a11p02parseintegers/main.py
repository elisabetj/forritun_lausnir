from insert_the_name_of_your_solution_file_here import list_to_int_tuple


def main():
    # You can use this for local testing:
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_like_autograder():
    test_input = prepare(input())
    return_value = list_to_int_tuple(test_input)
    print(return_value)


def prepare(test_input: str) -> list:
    return test_input.strip().split(",")


def run_samples():
    # Example usage
    run_sample_1()
    run_sample_2()


def run_sample_1():
    # Arrange.
    test_input = prepare("1,2,bla,42,52,62,t")
    expected = (1, 2, 42, 52, 62)

    # Act.
    actual = list_to_int_tuple(test_input)

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}):\n{test_input}\n",
            f"Expected output ({type(expected)}):\n{expected}\n",
            f"Actual output ({type(actual)}):\n{actual}",
        ]
    )
    print(message)
    assert expected == actual


def run_sample_2():
    # Arrange.
    test_input = prepare("1,-2,42,-5,3,2,-7")
    expected = (1, -2, 42, -5, 3, 2, -7)

    # Act.
    actual = list_to_int_tuple(test_input)

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}):\n{test_input}\n",
            f"Expected output ({type(expected)}):\n{expected}\n",
            f"Actual output ({type(actual)}):\n{actual}",
        ]
    )
    print(message)
    assert expected == actual


if __name__ == "__main__":
    main()
