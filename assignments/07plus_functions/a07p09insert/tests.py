from solution_code import insert_at

"""
Unit tests:

Test case 1:
Points: 2
"""

assert insert_at("abc", 0, "1") == "1abc"

"""
Test case 2:
Points: 2
"""

assert insert_at("abc", 3, "1") == "abc1"

"""
Test case 3:
Points: 1
"""

assert insert_at("abc", 2, "1") == "ab1c"
