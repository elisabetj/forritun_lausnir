#!/usr/bin/python3
import random
import sys
from string import ascii_letters
from typing import List

random.seed(sys.argv[-1])

MINIMUM_SCORE = 2000
VERY_HIGH_SCORE = 3000
MAXIMUM_SCORE = 3500


def main():
    number_of_lines = 100
    ratings = generate_ratings(number_of_lines)
    countries = generate_countries(number_of_lines)
    for i in range(number_of_lines):
        print(
            random_line(
                line_number=i + 1,
                country_code=countries[i],
                score=ratings[i],
            )
        )


def generate_ratings(number_of_lines: int) -> List[int]:
    """Generates a strictly decreasing list of ratings."""

    # First, randomly choose a low and high end of the list.
    minimum_difference = 2 * number_of_lines
    lowest = random.randint(MINIMUM_SCORE, VERY_HIGH_SCORE)
    highest = random.randint(lowest + minimum_difference, MAXIMUM_SCORE)
    difference = highest - lowest
    assert difference >= minimum_difference

    # Then distribute the values randomly on that interval,
    # such that all values are distinct.

    # Make sure the lead each player has on the next one is at least 1,
    # and that they sum up to the total difference between the highest and lowest rating.
    leads = [1 for _ in range(number_of_lines - 1)]
    for _ in range(difference - (number_of_lines - 1)):
        index = random.randrange(number_of_lines - 1)
        leads[index] += 1
    assert sum(leads) == difference
    assert lowest + sum(leads) == highest

    # Calculate ratings based on the leads between players.
    ratings = [highest]
    previous_rating = highest
    for lead in leads:
        next_rating = previous_rating - lead
        ratings.append(next_rating)
        previous_rating = next_rating

    # Now the list should be in descending order.
    assert lowest == ratings[-1] < ratings[0] == highest
    for i in range(number_of_lines - 1):
        assert ratings[i] > ratings[i + 1]

    return ratings


def generate_countries(number_of_lines: int) -> List[str]:
    assert number_of_lines > 3
    number_of_countries = random.randrange(3, number_of_lines)
    countries = [random_country_code() for _ in range(number_of_countries)]
    return random.choices(countries, k=number_of_lines)


def random_country_code():
    return "".join(random.choices(ascii_letters, k=3)).upper()


def random_line(line_number: int, country_code: str, score: int) -> str:
    rank = line_number
    first_name = random_name()
    last_name = random_name()
    birth_year = random_year()
    return f"{rank}; {last_name}, {first_name}; {country_code}; {score}; {birth_year}"


def random_name():
    return random_word().capitalize()


def random_word():
    length = random.randrange(2, 20)
    return "".join(random.choices(ascii_letters, k=length))


def random_year():
    return random.randint(1960, 2020)


if __name__ == "__main__":
    main()
