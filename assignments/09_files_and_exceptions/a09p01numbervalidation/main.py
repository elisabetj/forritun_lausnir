from solution_code import is_float


def main():
    run_like_gradescope()

    # You can use this for local testing:
    # run_samples()


def run_like_gradescope():
    test_input = input()
    print(is_float(test_input))


def run_samples():
    # Example usage
    print(is_float("3.45"))
    print(is_float("3e4"))
    print(is_float(".5"))
    print(is_float("abc"))
    print(is_float("4.x"))


if __name__ == "__main__":
    main()
