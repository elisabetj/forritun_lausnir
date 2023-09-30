import sys
from typing import Tuple


def determine_clearance(text: str, max_width: int) -> Tuple[int]:
    min_clearance_left = max_width
    min_clearance_right = max_width
    for line in text.splitlines():
        if not line:
            continue
        clearance_left = len(line) - len(line.lstrip(" "))
        min_clearance_left = min(clearance_left, min_clearance_left)
        clearance_right = max_width - len(line)
        min_clearance_right = min(clearance_right, min_clearance_right)

    return min_clearance_left, min_clearance_right


def change_indentation(text: str, spaces: int) -> str:
    """Adds or removes leading spaces to/from every line in the supplied string.

    A negative number of spaces instructs the function to remove spaces.
    A positive number of spaces instructs the function to add spaces.
    This function will automatically adjust the number of spaces
    to ensure that no line exceeds 80 characters.

    For example, if there's a line that's 78 characters long, and spaces = 4,
    then the function will only add 2 spaces to each line.

    Similarily, it will not remove more spaces than it can.
    If one line has only 2 leading spaces and spaces = -4,
    then the function will remove exactly 2 spaces from each line.
    """

    # Figure out how much clearance we have on the left and right
    MAX_WIDTH = 70
    clearance_left, clearance_right = determine_clearance(text, MAX_WIDTH)

    # Adjust the number of spaces added/removed, if needed, to ensure that the resulting string:
    # - stays within the maximum width when adding spaces
    # - doesn't remove any leading non-whitespace characters
    if spaces > 0:
        spaces = min(spaces, clearance_right)
    elif spaces < 0:
        spaces = max(spaces, clearance_left * -1)

    # Is there anything for us to do?
    if spaces == 0:
        return text  # Nope

    # Adjust indentation
    result = ""
    for line in text.splitlines():
        if spaces > 0:
            result += " " * spaces + line + "\n"
        elif spaces < 0:
            result += line[abs(spaces) :] + "\n"

    return result


if __name__ == "__main__":
    indent = int(input())
    text = sys.stdin.read()
    print(change_indentation(text, indent), end="")
