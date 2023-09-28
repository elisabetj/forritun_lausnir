from solution_code import move_one

"""
Unit tests:

Test case 1:
Points: 1
"""

assert move_one(1, 3, "321|||") == "32||1|"

"""
Test case 2:
Points: 2
"""

assert move_one(2, 3, "|321|4|") == "|32|41|"

"""
Test case 3:
Points: 2
"""

assert move_one(2, 1, "|21|543|") == "1|2|543|"
