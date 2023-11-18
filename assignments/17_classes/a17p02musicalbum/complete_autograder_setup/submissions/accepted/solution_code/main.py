#!/usr/bin/python3

from music_album import MusicAlbum


def main() -> None:
    requested_method = input()
    available_methods = {
        "__init__": create_album,
        "__str__": print_album,
    }
    assert (
        requested_method in available_methods
    ), f"Unexpected method {requested_method} requested."

    method_to_run = available_methods[requested_method]
    method_to_run()


def create_album():
    band = input()
    title = input()
    year = int(input())
    test_type = int(input())
    assert test_type in range(1, 9)

    if test_type == 1:
        album = MusicAlbum(band, title, year)
    elif test_type == 2:
        album = MusicAlbum(band=band)
    elif test_type == 3:
        album = MusicAlbum(title=title)
    elif test_type == 4:
        album = MusicAlbum(year=year)
    elif test_type == 5:
        album = MusicAlbum(band=band, title=title)
    elif test_type == 6:
        album = MusicAlbum(band=band, year=year)
    elif test_type == 7:
        album = MusicAlbum(title=title, year=year)
    else:
        assert test_type == 8
        album = MusicAlbum()

    print(
        f"Album created.",
        f" Band: {album.band}.",
        f" Title: {album.title}.",
        f" Year: {album.year}.",
        sep="\n",
    )

    return album


def print_album(album=None):
    if album is None:
        album = create_album()

    print(album)


if __name__ == "__main__":
    main()
