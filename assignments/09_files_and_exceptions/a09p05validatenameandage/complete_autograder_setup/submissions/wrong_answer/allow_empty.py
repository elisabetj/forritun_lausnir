MIN_AGE = 0
MAX_AGE = 125

NAME_PROMPT = "What's your name? "
INVALID_NAME_MESSAGE = "Please enter a valid name."

AGE_PROMPT = "How old are you? "
INVALID_AGE_MESSAGE = "Please enter an integer."
# It does not matter which values we use for the following constants,
# as long as they are unique.
# Here we use common status codes used in http, just for fun.
VALID_AGE = 200  # OK.
AGE_OUT_OF_RANGE = 406  # Not acceptable.
NON_NUMERIC_AGE = 400  # Bad request, apparent client error.


def main():
    name = get_valid_name()
    age = get_valid_age()
    print(f"Nice to meet you {name}. Congratulations on your {age} years.")


def get_valid_name():
    name = input(NAME_PROMPT)
    while not valid_name(name):
        print(INVALID_NAME_MESSAGE)
        name = input(NAME_PROMPT)
    return name


def valid_name(string):
    return all(x.isalpha() for x in string.replace(" ", ""))


def get_valid_age():
    age = input(AGE_PROMPT)

    while (response := validate_age(age)) != VALID_AGE:
        if response == AGE_OUT_OF_RANGE:
            print(f"You seriously expect me to believe you are {age} years old?")
        else:
            # Then we must have response == NON_NUMERIC_AGE,
            # since it is neither VALID_AGE nor AGE_OUT_OF_RANGE.
            # We can use the assert command to verify this assertion,
            # in case the program will be changed in the future
            # (this is called defensive programming).
            assert response == NON_NUMERIC_AGE
            print(INVALID_AGE_MESSAGE)

        age = input(AGE_PROMPT)

    return age


def validate_age(string):
    """Checks if age is valid, and returns status code indicating result."""

    try:
        age = int(string)
        if MIN_AGE <= age <= MAX_AGE:
            return VALID_AGE
        else:
            return AGE_OUT_OF_RANGE
    except ValueError:
        return NON_NUMERIC_AGE


if __name__ == "__main__":
    main()
