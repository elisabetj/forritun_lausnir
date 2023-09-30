from implementation import is_float


def main():
    run_for_gradescope()

    # Example usage
    # run_samples()


def run_for_gradescope():
    a = input()
    print(is_float(a))


def run_samples():
    print(is_float("3.45"))
    print(is_float("3e4"))
    print(is_float(".5"))
    print(is_float("abc"))
    print(is_float("4.x"))


if __name__ == "__main__":
    main()
