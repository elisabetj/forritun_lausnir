def sum_of_range(start: int, end: int, step: int) -> int:
    total_sum = 0

    term = start
    while term <= end:
        total_sum += term
        term += step

    return total_sum
