import sys


def main():
    # Simple test script.
    sys.stderr.write("Input music, group, singer: ")
    music, group, singer = input().split(",")

    state_music_opinion(music, group, singer)
    print()
    state_music_opinion()


# Definition for state_music_opinion goes here.


if __name__ == "__main__":
    main()
