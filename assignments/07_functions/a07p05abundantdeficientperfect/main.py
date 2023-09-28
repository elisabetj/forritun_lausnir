from solution_code import decide, sum_of_divisors


def main():
    # If you want the output to look exactly like in the problem statement,
    # you want to use this:

    # run_without_ui()

    # But for running the program interactively,
    # you might want to do something like this:

    run_with_ui()


def run_without_ui():
    number = int(input())
    decision = decide(number)
    print(decision)


def run_with_ui():
    number = int(input("Enter a number to check: "))
    divisor_sum = sum_of_divisors(number)
    print(
        f"The sum of all divisors of the number {number},",
        f"except for the number {number} itself,",
        f"is {divisor_sum}.",
        "Therefore,",
        sep="\n",
        end=" ",
    )
    verdict = decide(number)
    print(verdict)


if __name__ == "__main__":
    main()
