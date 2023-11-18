#!/usr/bin/python3

from music_album import MusicAlbum


def main():
    run_problem_statement_example()


def run_problem_statement_example():
    album = MusicAlbum()
    print(album)

    album.set_album("Talking Heads", "Remain in Light", 1980)
    print(album)

    album.set_album("AC/DC", "Back in Black")
    print(album)

    album_beatles = MusicAlbum("The Beatles", "Abbey Road")
    album_london_calling = MusicAlbum(title="London Calling", year=1979)
    album_beyonce = MusicAlbum(band="Beyonce", year=2016)

    print(album_beatles)
    print(album_london_calling)
    print(album_beyonce)


if __name__ == "__main__":
    main()
