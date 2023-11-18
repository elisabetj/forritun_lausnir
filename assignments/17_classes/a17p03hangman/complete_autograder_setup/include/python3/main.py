from importlib import import_module
from pathlib import Path

CLASS_NAME = "Hangman"


def main():
    test_hangman()


def test_hangman():
    Hangman = get_class()
    callables = {
        "__init__": test_hangman_init,
        "__str__": test_hangman_str,
        "guess_letter": test_guess_letter,
    }

    callable_name = input()
    callables[callable_name](Hangman)


def test_hangman_init(Hangman):
    assert hasattr(
        Hangman, "__init__"
    ), f"Could not find member function '__init__' of class 'Hangman'"

    parameters = Hangman.__init__.__code__.co_varnames
    assert len(parameters) == 2, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )

    word = input()

    try:
        instance = Hangman(word)
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    print(f"Hangman word created from the word '{word}'.")

    return instance


def test_hangman_str(Hangman):
    assert hasattr(
        Hangman, "__str__"
    ), f"Could not find member function '__str__' of class 'Hangman'"

    instance = test_hangman_init(Hangman)

    try:
        representation = str(instance)
    except Exception as e:
        print(f"Error getting string representation item: {e}")
        raise

    assert (
        representation is not None
    ), f"'__str__' method returned 'None', but should return a string."
    assert isinstance(
        representation, str
    ), f"'__str__' method returned '{type(representation)}', but should return 'str'."
    print(representation)


def test_guess_letter(Hangman):
    assert hasattr(
        Hangman, "guess_letter"
    ), f"Could not find member function 'guess_letter' of class 'Hangman'"

    instance = test_hangman_init(Hangman)
    print("Hangmand word before guess:")
    print(instance)

    letter = "a"
    try:
        result = instance.guess_letter(letter)
    except Exception as e:
        print(f"Error guessing letter: {e}")
        raise

    assert isinstance(result, bool), "\n".join(
        [
            f"Method 'guess_letter' did not return a boolean, as excpected.",
            f"Actual return type: {type(result)}",
            f"Actual return value: {result}",
        ]
    )

    print(f"Letter {letter} guessed.")
    print("Correctly." if result else "Incorrectly.")
    print("Hangmand word after guess:")
    print(instance)


def get_class(name=CLASS_NAME):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Could not find class {name}")


def load_modules():
    modules = []
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
