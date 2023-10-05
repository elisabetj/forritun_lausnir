"""This program computes a final score for a series of project scores:
Drops the lowest three scores, and sums the remaining scores.
"""
NUMBER_TO_DROP = 3


def main():
    scores = read_scores()
    if len(scores) < NUMBER_TO_DROP:
        print(f"At least {NUMBER_TO_DROP} scores needed!")
    else:
        for _ in range(len(scores)):
            remove_minimum(scores)
        print(f"Sum of scores ({NUMBER_TO_DROP} lowest removed): {round(sum(scores),1)}")


def read_scores() -> list:
    scores = input().strip().split()
    scores = [float(i) for i in scores]
    return scores


def remove_minimum(number_list: list) -> None:
    number_list.remove(min(number_list))

if __name__ == "__main__":
    main()
