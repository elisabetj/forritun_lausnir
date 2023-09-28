from solution_code import sum_of_range

"""
Unit tests:

Test case 1:
Points: 1
"""

result = sum_of_range(1, 10, 2)
assert result == 25

"""
Test case 2:
Points: 2
"""

result = sum_of_range(1, 10, 1)
assert result == 55

"""
Test case 3:
Points: 2
"""

result = sum_of_range(5, 10, 7)
assert result == 5
