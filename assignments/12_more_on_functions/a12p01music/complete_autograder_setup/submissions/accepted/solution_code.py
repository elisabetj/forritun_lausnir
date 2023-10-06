def main():
    music, group, singer = (choice.strip() for choice in input().split(","))
    call_function(music, group, singer)


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


def state_music_opinion(
    genre: str = "Classic Rock",
    music_group: str = "The Beatles",
    vocalist: str = "Freddie Mercury",
) -> None:
    print(f"The best type of music is {genre}.")
    print(f"The best music group is {music_group}.")
    print(f"The best lead vocalist is {vocalist}.")


if __name__ == "__main__":
    main()
