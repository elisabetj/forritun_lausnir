from solution_code import sum_of_range


def main():
    # If you want the output to look exactly like in the problem statement,
    # you want to use this:

    # run_like_samples()

    # But for running the program interactively,
    # you might want to do something like this:

    run_with_user_interface()


def run_like_samples():
    start = int(input())
    end = int(input())
    step = int(input())
    total = sum_of_range(start, end, step)
    print(total)


def run_with_user_interface():
    start = int(input("At what number should the sequence start? "))
    step = int(input("How much should the increase between consecutive terms be?"))
    end = int(input("After which point should the terms stop increasing? "))

    total = sum_of_range(start, end, step)

    print(
        f"The sum of the given sequence is {total}, because:",
        f"{start} + {start+step} + ... + {end} = {total}.",
        sep="\n",
    )


# Here is another useful convention,
# which we'll use from now on:
if __name__ == "__main__":
    main()

    # If someone wants to import your run_with_user_interface() function from this module,
    # they can just write:
    # from main import run_with_user_interface
    # but when that happens, the code in the module (this file) actually gets run.

    # If we want to be able to import the function
    # without running the code of this module immediately when the import happens,
    # we need to take some precautions.

    # You see, there is a special internal variable called __name__
    # associated with each module,
    # and when the module is imported, this variable holds the filename of the module.

    # But when the module is executed directly,
    # this variable gets the value "__main__" istead.

    # We can use this fact to check, at runtime,
    # whether the module is being imported or run on its own.

    # Then we just wrap the actual call to main() inside this if statement,
    # so it only gets called if the module is being executed as a program,
    # not when it is being imported, or some of its content is.
