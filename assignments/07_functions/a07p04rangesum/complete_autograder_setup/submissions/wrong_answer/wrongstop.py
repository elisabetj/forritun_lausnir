def sum_of_range(start: int, end: int, step: int) -> int:
    total_sum = 0
    for number in range(start, end, step):
        total_sum += number

    return total_sum
