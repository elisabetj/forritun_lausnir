from solution_code import prime_sum


def main():
    # You can use this for local testing:
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_like_autograder():
    test_input = get_list()
    return_value = prime_sum(test_input)
    print(return_value)


def get_list() -> list:
    """Gets numbers from user."""

    user_input = input()
    return prepare(user_input)


def prepare(test_input: str) -> list:
    a_list_of_strings = test_input.strip().split(",")
    a_list_of_ints = [int(number) for number in a_list_of_strings]
    return a_list_of_ints


def run_samples():
    # Example usage
    run_sample_1()
    run_sample_2()
    run_sample_3()


def run_sample_1():
    test(
        test_input=prepare("1,2,3,4,5,6,7,8,9,10,11"),
        expected=28,
    )


def run_sample_2():
    test(
        test_input=prepare("4,6,12,32"),
        expected=0,
    )


def run_sample_3():
    test(
        test_input=prepare("2,4,6,12,32,64,120"),
        expected=2,
    )


def test(test_input, expected):
    # Act.
    actual = prime_sum(test_input)

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput ({type(test_input)}):\n{test_input}\n",
            f"Expected output ({type(expected)}): {expected}",
            f"Actual output ({type(actual)}): {actual}",
        ]
    )
    # print(message)  # Uncomment this to see message even when passed.
    assert expected == actual, message


if __name__ == "__main__":
    main()
