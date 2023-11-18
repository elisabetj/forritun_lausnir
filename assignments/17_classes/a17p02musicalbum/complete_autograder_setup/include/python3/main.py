from importlib import import_module
from pathlib import Path

CLASS_NAME = "MusicAlbum"


def main():
    test_musicalbum()


def test_musicalbum():
    MusicAlbum = get_class()
    callables = {
        "__init__": test_musicalbum_init,
        "__str__": test_musicalbum_str,
    }

    callable_name = input()
    callables[callable_name](MusicAlbum)


def test_musicalbum_init(MusicAlbum):
    assert hasattr(
        MusicAlbum, "__init__"
    ), f"Could not find member function '__init__' of class 'MusicAlbum'"

    parameters = MusicAlbum.__init__.__code__.co_varnames
    assert "band" in parameters, (
        f"Could not find parameter 'band'"
        "in member function '__init__' of class 'MusicAlbum'.",
    )
    assert "title" in parameters, (
        f"Could not find parameter 'title'"
        "in member function '__init__' of class 'MusicAlbum'.",
    )
    assert "year" in parameters, (
        f"Could not find parameter 'year'"
        "in member function '__init__' of class 'MusicAlbum'.",
    )
    assert len(parameters) == 4, (
        f"Unexpected number of parameters, {len(parameters)}.",
    )
    assert (
        parameters[1] == "band"
    ), f"Parameter 'band' not found in its expected position."
    assert (
        parameters[2] == "title"
    ), f"Parameter 'title' not found in its expected position."
    assert (
        parameters[3] == "year"
    ), f"Parameter 'year' not found in its expected position."

    band = input()
    title = input()
    year = int(input())
    test_type = int(input())

    try:
        if test_type == 1:
            instance = MusicAlbum(band, title, year)
        elif test_type == 2:
            instance = MusicAlbum(band=band)
        elif test_type == 3:
            instance = MusicAlbum(title=title)
        elif test_type == 4:
            instance = MusicAlbum(year=year)
        elif test_type == 5:
            instance = MusicAlbum(band=band, title=title)
        elif test_type == 6:
            instance = MusicAlbum(band=band, year=year)
        elif test_type == 7:
            instance = MusicAlbum(title=title, year=year)
        else:
            assert test_type == 8
            instance = MusicAlbum()
    except Exception as e:
        print(f"Error calling constructor: {e}")
        raise

    for attribute in "band", "title", "year":
        assert hasattr(instance, attribute), (
            f"Could not find attribute '{attribute}'"
            "in instance of class 'MusicAlbum'."
        )

    print(
        f"Album created.",
        f" Band: {instance.band}.",
        f" Title: {instance.title}.",
        f" Year: {instance.year}.",
        sep="\n",
    )

    return instance


def test_musicalbum_str(MusicAlbum) -> None:
    assert hasattr(
        MusicAlbum, "__str__"
    ), f"Could not find member function '__str__' of class 'MusicAlbum'"

    instance = test_musicalbum_init(MusicAlbum)

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
