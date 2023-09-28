from solution_code import is_substring_of

"""
Test case 1:
"""

result = is_substring_of("python", "There's a python in my boot!")
assert result == True

"""
Test case 2:
"""

result = is_substring_of("This is definitely not a substring", "It really isn't")
assert result == False

"""
Test case 3:
"""

result = is_substring_of(
    "python",
    "I've had it with these motherf***ing pythons on this motherf***ing plane!",
)
assert result == True

"""
Test case 4:
"""

result = is_substring_of("", "Empty?")
assert result == True

"""
Test case 5:
"""

result = is_substring_of(" ", "Space?")
assert result == False
