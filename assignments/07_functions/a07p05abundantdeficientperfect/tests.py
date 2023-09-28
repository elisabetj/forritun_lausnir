from solution_code import decide, sum_of_factors

"""
Unit tests:

Test case 1:
Points: 1
"""

result = decide(6)
assert result == "6 is a perfect number."

"""
Test case 2:
Points: 1
"""

result = sum_of_factors(6)
assert result == 6

"""
Test case 3:
Points: 1
"""

result = decide(10)
assert result == "10 is deficient."

"""
Test case 4:
Points: 1
"""

result = sum_of_factors(10)
assert result == 8

"""
Test case 5:
"""

result = decide(66)
assert result == "66 is abundant."

"""
Test case 6:
"""

result = sum_of_factors(66)
assert result == 78
