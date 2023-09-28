from solution_code import extract_first_number_from_string

"""
Test case 1:
Points: 2
"""

result = extract_first_number_from_string("There are 365 or 366 days in the year.")
assert result == 365

"""
Test case 2:
Points: 2
"""

result = extract_first_number_from_string(
    "These are not the numbers you are looking for."
)
assert result == -1

"""
Test case 3:
Points: 1
"""

result = extract_first_number_from_string("")
assert result == -1
