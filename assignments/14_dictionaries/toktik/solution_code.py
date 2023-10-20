#!/usr/env/bin python3

from typing import Dict


def main():
    popularity = tally_views()
    star = determine_leader(popularity)
    print(star)


def tally_views() -> Dict[str, int]:
    view_counts = {}

    number_of_videos = int(input())
    for video in range(number_of_videos):
        name_of_uploader, how_often_viewed = input().strip().split()
        number_of_views = int(how_often_viewed)

        if name_of_uploader not in view_counts:
            view_counts[name_of_uploader] = 0

        view_counts[name_of_uploader] += number_of_views

    return view_counts


def determine_leader(view_counts: Dict[str, int]) -> str:
    highest_number_of_views = 0
    most_popular = ""

    for content_creator, views in view_counts.items():
        if views > highest_number_of_views:
            most_popular = content_creator
            highest_number_of_views = views

    return most_popular


if __name__ == "__main__":
    main()
