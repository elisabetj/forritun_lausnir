from importlib import import_module
from pathlib import Path


def main():
    # Arrange.
    function_name = "state_music_opinion"
    state_music_opinion = get_function(function_name)
    expected = None
    music, band, singer = (choice.strip() for choice in input().split(","))

    # Act.
    if music:
        if band:
            if singer:
                actual = state_music_opinion(music, band, singer)
            else:
                actual = state_music_opinion(genre=music, music_group=band)
        else:
            if singer:
                actual = state_music_opinion(genre=music, vocalist=singer)
            else:
                actual = state_music_opinion(genre=music)
    else:
        if band:
            if singer:
                actual = state_music_opinion(music_group=band, vocalist=singer)
            else:
                actual = state_music_opinion(music_group=band)
        else:
            if singer:
                actual = state_music_opinion(vocalist=singer)
            else:
                actual = state_music_opinion()

    # Assert.
    message = "\n".join(
        [
            f"\n\nInput to function '{function_name}':",
            f" genre ({type(music)}):\n{music}\n",
            f" music_group ({type(band)}):\n{band}\n",
            f" vocalist ({type(singer)}):\n{singer}\n",
            f"Expected output ({type(expected)}): {expected}",
            f"Actual output ({type(actual)}): {actual}",
        ]
    )
    assert expected == actual, message


def get_function(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Name '{name}' is not defined.")


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
