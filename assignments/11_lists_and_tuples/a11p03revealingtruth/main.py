from insert_the_name_of_your_solution_file_here import list_to_bool_tuple


def main():
    # You can use this for local testing:
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_like_autograder():
    test_input = prepare(input())
    return_value = list_to_bool_tuple(test_input)
    print(return_value)


def prepare(test_input: str) -> list:
    return test_input.strip().split(",")


def run_samples():
    # Example usage
    run_sample_1()
    run_sample_2()
    run_sample_3()


def run_sample_1():
    # Arrange.
    test_input = prepare("1,2,bla,42,52,,0,,t,,,")
    expected = (
        True,
        True,
        True,
        True,
        True,
        False,
        False,
        False,
        True,
        False,
        False,
        False,
    )

    # Act.
    actual = list_to_bool_tuple(test_input)

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
    test_input = prepare("0,,1,10,-1")
    expected = (False, False, True, True, True)

    # Act.
    actual = list_to_bool_tuple(test_input)

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}):\n{test_input}\n",
            f"Expected output ({type(expected)}):\n{expected}\n",
            f"Actual output ({type(actual)}):\n{actual}",
        ]
    )
    # print(message)
    assert expected == actual, message


def run_sample_3():
    # Arrange.
    test_input = ["1", "2", "3"]
    expected_type = tuple

    # Act.
    actual = list_to_bool_tuple(test_input)

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}):\n{test_input}\n",
            f"Expected type of output: {expected_type}",
            f"Actual output ({type(actual)}):\n{actual}\n",
            "Return type of list_to_bool_tuple is not a tuple.",
        ]
    )
    assert expected_type == type(actual), message


if __name__ == "__main__":
    main()
