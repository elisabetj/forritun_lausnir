from solution_code import remove_at

"""
Unit tests:

Test case 1:
Points: 2
"""

state = "321|||"
state, removed = remove_at(state, 2)
assert state == "32|||"
assert removed == "1"


"""
Test case 2:
Points: 2
"""

state = "3|21||"
state, removed = remove_at(state, 0)
assert state == "|21||"
assert removed == "3"


"""
Test case 3:
Points: 1
"""

state = "3|21||"
state, removed = remove_at(state, 5)
assert state == "3|21|"
assert removed == "|"
