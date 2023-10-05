"""This program computes a final score for a series of project scores:
Drops the lowest three scores, and sums the remaining scores.
"""
NUMBER_TO_DROP = 3


def main():
    scores = read_scores()
    if len(scores) < NUMBER_TO_DROP:
        print(f"At least {NUMBER_TO_DROP} scores needed!")
    else:
        for _ in range(NUMBER_TO_DROP):
            remove_minimum(scores)
        sum_scores = ""
        for score in scores:
            sum_scores += score
        print(f"Sum of scores ({NUMBER_TO_DROP} lowest removed): {sum_scores}")


def read_scores() -> list:
    scores = input().strip().split()
    scores = [i for i in scores]
    return scores


def remove_minimum(number_list: list) -> None:
    number_list.remove(min(number_list))

if __name__ == "__main__":
    main()
