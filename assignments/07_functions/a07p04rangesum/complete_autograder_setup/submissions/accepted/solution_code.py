def sum_of_range(start: int, end: int, step: int) -> int:
    total_sum = 0
    for number in range(start, end + 1, step):
        total_sum += number

    return total_sum


if __name__ == "__main__":
    start = int(input())
    end = int(input())
    step = int(input())
    print(sum_of_range(start, end, step))
