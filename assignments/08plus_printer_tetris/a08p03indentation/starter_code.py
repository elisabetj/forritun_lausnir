def change_indentation(text: str, spaces: int) -> str:
    """Adds or removes leading spaces to/from every line in the supplied string.

    A negative number of spaces instructs the function to remove spaces.
    A positive number of spaces instructs the function to add spaces.
    This function will automatically adjust the number of spaces
    to ensure that no line exceeds 70 characters.

    For example, if there's a line that's 68 characters long, and spaces = 4,
    then the function will only add 2 spaces to each line.

    Similarily, it will not remove more spaces than it can.
    If one line has only 2 leading spaces and spaces = -4,
    then the function will remove exactly 2 spaces from each line.
    """

    # ... now add your code
