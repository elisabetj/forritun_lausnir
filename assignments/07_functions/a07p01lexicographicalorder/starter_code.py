# Note, a good practice is to annotate the types of the input and output in the function header.
# This is not strictly necessary for the code to run, but is a recommended practice,
# for readability purposes as well as having other benefits,
# such as allowing automatic tools to gain more information about the intent of the code,
# and use that information to provide better suggestions to the programmer among other things.
def precedes(first: str, second: str) -> str:
    """Returns the string that comes first in lexicographical order.

    Ignores case.
    """
    # The above string is what is called a doc-string, or documentation string,
    # and it is good practice to place one at the start of (almost) all functions.

    # Your implementation goes here
