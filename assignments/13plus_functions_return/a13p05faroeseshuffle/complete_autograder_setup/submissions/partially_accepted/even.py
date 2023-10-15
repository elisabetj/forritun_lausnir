def shuffle(original_list: list, start_from_back: bool = False) -> list:
    """Returns a shuffled copy of the supplied list. The original list is not modified.

    Let n denote the length of the list. The shuffled order is then as follows:
    0, n-1, 1, n-2, 2 ... and so forth

    If start_from_back == True then the shuffled order is:
    n-1, 0, n-2, 1, n-3 ... and so forth

    Only works for even length lists due to bug.
    """
    result = []
    length = len(original_list)

    for i in range(length//2):
        location_front = i
        location_back = length - 1 - i

        if start_from_back:
            result.append(original_list[location_back])
        result.append(original_list[location_front])
        if not start_from_back:
            result.append(original_list[location_back])

    return result

def main():
    start_from_back = input() == "bottom"
    length = int(input())
    deck = list(map(int, input().split()))
    shuffled_deck = shuffle(deck, start_from_back)
    print(' '.join([str(label) for label in shuffled_deck]))

if __name__ == "__main__":
    main()
