#!/usr/bin/python3

import random
import sys
from typing import List

YATZY = 0
NOT_YATZY = 1

random.seed(sys.argv[-1])

# Groups:
# 5                    Yatzy.
# 3 + 1 + 1            3 of a kind, simple.
# 2 + 1 + 1 + 1        2 of a kind, simple.
# 2 + 2 + 1            2 of a kind, double.
# 1 + 1 + 1 + 1 + 1.   All different.
# 4 + 1                3 of a kind, with 1 extra.
# 3 + 2                3 of a kind, with a pair on the side.

# New API:
# 1: Minimum number of lines.
# 2: Maximum number of lines.
# 3: Min number of Yatzy rolls.
# 4: Max number of Yatzy rolls.
# 5: Min number of Simple-3.
# 6: Max number of Simple-3.
# 7: Min number of Simple-2.
# 8: Max number of Simple-2.
# 9: Min number of Double-2.
# 10: Max number of Double-2.
# 11: Min number of All-different.
# 12: Max number of All-different.
# 13: Min number of 4+1.
# 14: Max number of 4+1.
# 15: Min number of 3+2.
# 16: Max number of 3+2.

DEFAULT_MIN = 0
DEFAULT_MAX = 20

MIN_LINES = int(sys.argv[1]) if len(sys.argv) > 2 else DEFAULT_MIN
MAX_LINES = int(sys.argv[2]) if len(sys.argv) > 3 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_LINES <= MAX_LINES <= DEFAULT_MAX

MIN_YATZY = int(sys.argv[3]) if len(sys.argv) > 4 else DEFAULT_MIN
MAX_YATZY = int(sys.argv[4]) if len(sys.argv) > 5 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_YATZY <= MAX_YATZY <= DEFAULT_MAX

MIN_3_1_1 = int(sys.argv[5]) if len(sys.argv) > 6 else DEFAULT_MIN
MAX_3_1_1 = int(sys.argv[6]) if len(sys.argv) > 7 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_3_1_1 <= MAX_3_1_1 <= DEFAULT_MAX

MIN_2_1_1_1 = int(sys.argv[7]) if len(sys.argv) > 8 else DEFAULT_MIN
MAX_2_1_1_1 = int(sys.argv[8]) if len(sys.argv) > 9 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_2_1_1_1 <= MAX_2_1_1_1 <= DEFAULT_MAX

MIN_2_2_1 = int(sys.argv[9]) if len(sys.argv) > 10 else DEFAULT_MIN
MAX_2_2_1 = int(sys.argv[10]) if len(sys.argv) > 11 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_2_2_1 <= MAX_2_2_1 <= DEFAULT_MAX

MIN_VOID = int(sys.argv[11]) if len(sys.argv) > 12 else DEFAULT_MIN
MAX_VOID = int(sys.argv[12]) if len(sys.argv) > 13 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_VOID <= MAX_VOID <= DEFAULT_MAX

MIN_4_1 = int(sys.argv[13]) if len(sys.argv) > 14 else DEFAULT_MIN
MAX_4_1 = int(sys.argv[14]) if len(sys.argv) > 15 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_4_1 <= MAX_4_1 <= DEFAULT_MAX

MIN_3_2 = int(sys.argv[15]) if len(sys.argv) > 16 else DEFAULT_MIN
MAX_3_2 = int(sys.argv[16]) if len(sys.argv) > 17 else DEFAULT_MAX
assert DEFAULT_MIN <= MIN_3_2 <= MAX_3_2 <= DEFAULT_MAX

assert (
    MIN_LINES
    <= MAX_YATZY + MAX_3_1_1 + MAX_2_1_1_1 + MAX_2_2_1 + MAX_VOID + MAX_4_1 + MAX_3_2
)
MIN_REQUIREMENTS = (
    MIN_YATZY + MIN_3_1_1 + MIN_2_1_1_1 + MIN_2_2_1 + MIN_VOID + MIN_4_1 + MIN_3_2
)
if MIN_LINES < MIN_REQUIREMENTS:
    MIN_LINES = MIN_REQUIREMENTS

MAX_REQUIREMENTS = (
    MAX_YATZY + MAX_3_1_1 + MAX_2_1_1_1 + MAX_2_2_1 + MAX_VOID + MAX_4_1 + MAX_3_2
)
if MAX_LINES > MAX_REQUIREMENTS:
    MAX_LINES = MAX_REQUIREMENTS

assert MIN_LINES <= MAX_LINES


def main():
    number_of_lines = random.randint(MIN_LINES, MAX_LINES)

    # First, fullfill the minimum requirements
    yatzy_rolls = [roll_yatzee() for _ in range(MIN_YATZY)]
    four_of_a_kind_rolls = [roll_4_1() for _ in range(MIN_4_1)]
    full_house_rolls = [roll_3_2() for _ in range(MIN_3_2)]
    three_of_a_kind_rolls = [roll_3_1_1() for _ in range(MIN_3_1_1)]
    two_pairs_rolls = [roll_2_2_1() for _ in range(MIN_2_2_1)]
    pair_rolls = [roll_2_1_1_1() for _ in range(MIN_2_1_1_1)]
    void_rolls = [roll_void() for _ in range(MIN_VOID)]

    dice_rolls = (
        yatzy_rolls
        + four_of_a_kind_rolls
        + full_house_rolls
        + three_of_a_kind_rolls
        + two_pairs_rolls
        + pair_rolls
        + void_rolls
    )
    additional_rolls_required = number_of_lines - len(dice_rolls)

    # Then fill up with anything available, while respecting the maximum requirements.
    yatzy_rolls = [roll_yatzee() for _ in range(MAX_YATZY - MIN_YATZY)]
    four_of_a_kind_rolls = [roll_4_1() for _ in range(MAX_4_1 - MIN_4_1)]
    full_house_rolls = [roll_3_2() for _ in range(MAX_3_2 - MIN_3_2)]
    three_of_a_kind_rolls = [roll_3_1_1() for _ in range(MAX_3_1_1 - MIN_3_1_1)]
    two_pairs_rolls = [roll_2_2_1() for _ in range(MAX_2_2_1 - MIN_2_2_1)]
    pair_rolls = [roll_2_1_1_1() for _ in range(MAX_2_1_1_1 - MIN_2_1_1_1)]
    void_rolls = [roll_void() for _ in range(MAX_VOID - MIN_VOID)]

    extra_rolls = (
        yatzy_rolls
        + four_of_a_kind_rolls
        + full_house_rolls
        + three_of_a_kind_rolls
        + two_pairs_rolls
        + pair_rolls
        + void_rolls
    )
    random.shuffle(extra_rolls)
    fill = extra_rolls[:additional_rolls_required]
    dice_rolls.extend(fill)
    assert len(dice_rolls) == number_of_lines

    random.shuffle(dice_rolls)
    for dice_roll in dice_rolls:
        print(make_line(dice_roll))

    print()  # Empty line at the end.


def roll_yatzee() -> List[str]:
    quintuple = str(random.randint(1, 6))
    dice_roll = [quintuple] * 5

    assert len(dice_roll) == 5
    return dice_roll


def roll_4_1() -> List[str]:
    quadruple, single = get_different_dice_results(how_many=2)

    dice_roll = [quadruple] * 4 + [single]
    random.shuffle(dice_roll)

    assert len(dice_roll) == 5
    return dice_roll


def roll_3_2() -> List[str]:
    triple, double = get_different_dice_results(how_many=2)

    dice_roll = [triple] * 3 + [double] * 2
    random.shuffle(dice_roll)

    assert len(dice_roll) == 5
    return dice_roll


def roll_3_1_1() -> List[str]:
    triple, first_single, second_single = get_different_dice_results(how_many=3)

    dice_roll = [triple] * 3 + [first_single] + [second_single]
    random.shuffle(dice_roll)

    assert len(dice_roll) == 5
    return dice_roll


def roll_2_2_1() -> List[str]:
    first_double, second_double, single = get_different_dice_results(how_many=3)

    dice_roll = [first_double] * 2 + [second_double] * 2 + [single]
    random.shuffle(dice_roll)

    assert len(dice_roll) == 5
    return dice_roll


def roll_2_1_1_1() -> List[str]:
    double, single1, single2, single3 = get_different_dice_results(how_many=4)

    dice_roll = [double] * 2 + [single1] + [single2] + [single3]
    random.shuffle(dice_roll)

    assert len(dice_roll) == 5
    return dice_roll


def roll_void() -> List[str]:
    dice_roll = get_different_dice_results(how_many=5)

    assert len(dice_roll) == 5
    return dice_roll


def get_different_dice_results(how_many: int) -> List[str]:
    possibilities = [str(value + 1) for value in range(6)]
    random.shuffle(possibilities)
    return [possibilities.pop() for _ in range(how_many)]


def make_line(dice_roll: List[str]) -> str:
    return " ".join(dice_roll)


if __name__ == "__main__":
    main()
