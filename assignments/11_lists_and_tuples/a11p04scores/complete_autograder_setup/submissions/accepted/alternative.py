"""This program computes a final score for a series of project scores:
Drops the lowest three scores, and sums the remaining scores.
"""
NUMBER_TO_DROP = 3


def main():
    scores = read_scores()
    if len(scores) < NUMBER_TO_DROP:
        print(f"At least {NUMBER_TO_DROP} scores needed!")
        return

    assert len(scores) >= NUMBER_TO_DROP
    for _ in range(NUMBER_TO_DROP):
        remove_minimum(scores)

    print(f"Sum of scores ({NUMBER_TO_DROP} lowest removed): {round(sum(scores),1)}")


def read_scores() -> list:
    scores = input().strip().split()
    scores = [float(i) for i in scores]
    return scores


def remove_minimum(number_list: list) -> None:
    assert len(number_list) > 0

    index_of_smallest_element = 0
    for i in range(1, len(number_list)):
        if number_list[i] < number_list[index_of_smallest_element]:
            index_of_smallest_element = i
    number_list.pop(index_of_smallest_element)


if __name__ == "__main__":
    main()
