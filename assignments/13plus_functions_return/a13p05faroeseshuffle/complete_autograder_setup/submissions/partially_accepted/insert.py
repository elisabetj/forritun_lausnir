def shuffle(original_list: list, start_from_back: bool = False) -> list:
    """Returns a shuffled copy of the supplied list. The original list is not modified.

    Let n denote the length of the list. The shuffled order is then as follows:
    0, n-1, 1, n-2, 2 ... and so forth

    If start_from_back == True then the shuffled order is:
    n-1, 0, n-2, 1, n-3 ... and so forth
    """
    result = []
    length = len(original_list)

    for i in range(0, length, 2):
        location = i // 2
        result.append(original_list[location])

    insertion_index = 0 if start_from_back else 1
    location = length - 1
    while location > (length - 1) // 2:
        result.insert(insertion_index, original_list[location])
        location -= 1
        insertion_index += 2

    return result

def main():
    start_from_back = input() == "bottom"
    length = int(input())
    deck = list(map(int, input().split()))
    shuffled_deck = shuffle(deck, start_from_back)
    print(' '.join([str(label) for label in shuffled_deck]))

if __name__ == "__main__":
    main()
