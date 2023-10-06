from typing import List


def main():
    int_list = [int(string) for string in input().split()]
    print(f"Original list before calling functions: {int_list}")
    result = extract_evens(int_list)
    print(f"Resulting list after extracting evens: {result}")
    print(f"Original list after extracting evens and before removing odds: {int_list}")
    remove_odds(int_list)
    print(f"Original list after removing odds: {int_list}")


def remove_odds(int_list: List[int]) -> None:
    """Removes odd integers from the given list."""

    # Any of the following works
    remove_odds_1(int_list)
    # remove_odds_2(int_list)
    # remove_odds_3(int_list)
    # remove_odds_4(int_list)
    # remove_odds_5(int_list)
    # remove_odds_6(int_list)
    # remove_odds_7(int_list)
    # remove_odds_8(int_list)


def remove_odds_1(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a copy first, for reference.
    Iterates over the reference, and modifies the original.
    """

    a_copy = make_a_copy(int_list)

    # We use the copy as a reference that stays unchanged while we iterate over it.
    for num in a_copy:
        if num % 2 == 1:
            int_list.remove(num)

    # If we would instead iterate over int_list itself,
    # and also modify int_list while we are iterating over it:
    #
    # for num in int_list:
    #     if num % 2 == 1:
    #         int_list.remove(num)
    #
    # then we run into problems, because if we remove a number from the list,
    # then the rest of the list will move one seat to the left.
    # But the index also moves one seat to the right,
    # and thus will skip over the next element in the list.
    # That's no good.


def make_a_copy(int_list: List[int]) -> List[int]:
    """Returns a copy of the given list.

    Demonstrates various ways to copy lists.
    """

    # There are various ways to make a copy. The following all work
    a_copy = int_list[:]
    a_copy = [num for num in int_list]
    a_copy = int_list.copy()
    a_copy = list(int_list)

    # You can also use the copy package.
    # Normally we want to keep imports at the top of the file,
    # but this is just for demonstration purposes,
    # so we keep it here within easy reach.
    from copy import copy

    a_copy = copy(int_list)

    # These all make only shallow copies though,
    # which works fine when the lists are not nested,
    # such as lists of integers, like in this case.

    # For nested lists (or more generally lists that have mutable objects as elements),
    # you want to use deepcopy instead:
    from copy import deepcopy

    complete_copy = deepcopy(int_list)

    # This way does not work:
    not_a_copy = int_list  # if we modify not_a_copy, then we also modify int_list.

    return a_copy


def remove_odds_2(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Iterates backwards over the list, so it can safely modify the list on the fly.
    """

    for num in int_list[::-1]:
        if num % 2 == 1:
            int_list.remove(num)

    # Here, if we remove an element from the list,
    # it doesn't affect the index of any elements that remain to be seen,
    # because they are all further left.
    #
    # And in case the same number appears more than once,
    # then we'll remove the first occurrence instead,
    # but that's all right, because then the occurrence we just saw
    # will move one seat to the left also,
    # so we'll see it again immediately in the next step,
    # and try to remove it again.
    # This is repeated until it becomes the last occurence of the number,
    # and then itself will be removed,
    # and we continue on to the next number to the left.


def remove_odds_3(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Takes care not to move on to the next index
    at the same time as the rest of the list is moved backwards
    (thus skipping over one element).
    """

    for i in range(len(int_list)):
        while i < len(int_list) and int_list[i] % 2 == 1:
            int_list.pop(i)


def remove_odds_4(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Takes care not to move on to the next index
    at the same time as the rest of the list is moved backwards
    (thus skipping over one element).
    """

    for i, _ in enumerate(int_list):
        while i < len(int_list) and int_list[i] % 2 == 1:
            int_list.pop(i)


def remove_odds_5(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Takes care not to move on to the next index
    at the same time as the rest of the list is moved backwards
    (thus skipping over one element).
    """

    i = 0
    while i < len(int_list):
        if int_list[i] % 2 == 1:
            int_list.pop(i)
        else:
            i += 1


def remove_odds_6(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a new list with the even numbers only,
    and then modifies the original list to match.
    """

    only_evens = [num for num in int_list if num % 2 == 0]

    i = 0
    # Copy the correct list into the original, one even number at a time.
    while i < len(only_evens):
        int_list[i] = only_evens[i]
        i += 1

    # And make sure to cut off anything that has not already been overwritten.
    while len(int_list) > len(only_evens):
        int_list.pop()


def remove_odds_7(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a new list with the even numbers only,
    and then modifies the original list to match.
    """

    only_evens = [num for num in int_list if num % 2 == 0]

    # Begin by completely emptying the original list.
    while int_list:
        int_list.pop()

    # Then repopulate it with the correct values.
    for even in only_evens:
        int_list.append(even)


def remove_odds_8(int_list: List[int]) -> None:
    """Removes odd integers from the given list.

    Makes a new list with the even numbers only,
    and then modifies the original list to match.
    """

    only_evens = [num for num in int_list if num % 2 == 0]

    # Simply replace all the contents of the original list with the new one.
    int_list[:] = only_evens


def extract_evens(int_list: List[int]) -> List[int]:
    """Returns a new list with only the even integers from the given list."""

    return [number for number in int_list if number % 2 == 0]


if __name__ == "__main__":
    main()
