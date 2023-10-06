from typing import Tuple

from solution_code import state_music_opinion


def main():
    # You can use this for local testing:
    run_samples()

    # Or run this to take input from terminal:
    run_like_autograder()


def run_like_autograder():
    music, band, singer = ask_opinion()
    call_function(music, band, singer)


def ask_opinion() -> Tuple:
    """Gets numbers from user."""

    user_input = input()
    return prepare(user_input)


def prepare(test_input: str) -> Tuple:
    return tuple(choice.strip() for choice in test_input.split(","))


def call_function(music, band, singer):
    if music:
        if band:
            if singer:
                state_music_opinion(music, band, singer)
            else:
                state_music_opinion(genre=music, music_group=band)
        else:
            if singer:
                state_music_opinion(genre=music, vocalist=singer)
            else:
                state_music_opinion(genre=music)
    else:
        if band:
            if singer:
                state_music_opinion(music_group=band, vocalist=singer)
            else:
                state_music_opinion(music_group=band)
        else:
            if singer:
                state_music_opinion(vocalist=singer)
            else:
                state_music_opinion()


def run_samples():
    # Example usage
    run_sample_1()
    run_sample_2()
    run_sample_3()
    run_sample_4()
    run_sample_5()
    run_sample_6()


def run_sample_1():
    print("\nTest case 1\n")
    test(
        test_input=prepare("Rythm and blues,Greta Van Fleet,Luciano Pavarotti"),
        expected=prepare("Rythm and blues, Greta Van Fleet, Luciano Pavarotti"),
    )


def run_sample_2():
    print("\nTest case 2\n")
    test(
        test_input=prepare("Classical music,Uriah Heep,David Bowie"),
        expected=prepare("Classical music, Uriah Heep, David Bowie"),
    )


def run_sample_3():
    print("\nTest case 3\n")
    test(
        test_input=prepare("Heavy metal,Simon & Garfunkel,Linda Perry"),
        expected=prepare("Heavy metal, Simon & Garfunkel, Linda Perry"),
    )


def run_sample_4():
    print("\nTest case 4\n")
    test(
        test_input=prepare(",Simon & Garfunkel,"),
        expected=prepare("Classic Rock, Simon & Garfunkel, Freddie Mercury"),
    )


def run_sample_5():
    print("\nTest case 5\n")
    test(
        test_input=prepare("Classical music,,Linda Perry"),
        expected=prepare("Classical music, The Beatles, Linda Perry"),
    )


def run_sample_6():
    print("\nTest case 6\n")
    test(
        test_input=prepare(",,"),
        expected=prepare("Classic Rock, The Beatles, Freddie Mercury"),
    )


def test(test_input, expected):
    # Arrange.
    music, band, singer = test_input

    # Act.
    call_function(music, band, singer)

    # Assert.
    #
    # The function does not return anything,
    # so we cannot really test that it prints what it is supposed to,
    # without going through some extra trouble
    # like diverting the standard output to a file to check,
    # which is what is commonly done when autograding.
    #
    # We could verify that the function returns None,
    # and Gradescope does that too,
    # but the usefuleness of that by itself is limited.
    #
    # But you can of course examine the output manually,
    # and compare it to what is excpected.
    message = "\n".join(
        [
            f"\n\nInput to function 'state_music_opinion':",
            f" genre ({type(music)}):\n{music}\n",
            f" music_group ({type(band)}):\n{band}\n",
            f" vocalist ({type(singer)}):\n{singer}\n",
            f"Expected choices to appear in output:\n{expected}\n",
            f"Compare the actual output above with the following:\n",
        ]
    )
    print(message)
    music, band, singer = expected
    state_music_opinion(genre=music, music_group=band, vocalist=singer)


if __name__ == "__main__":
    main()
