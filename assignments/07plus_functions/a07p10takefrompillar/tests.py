from solution_code import take_from_pillar

"""
Unit tests:

Test case 1:
Points: 2
"""

state = "3|2|1|"
new_state, removed = take_from_pillar(state, 3)
assert new_state == "3|2||"
assert removed == "1"

"""
Test case 2:
Points: 2
"""

state = "32||1|"
state, removed = take_from_pillar(state, 1)
assert state == "3||1|"
assert removed == "2"

"""
Test case 3:
Points: 1
"""

state = "|43|521|"
state, removed = take_from_pillar(state, 2)
assert state == "|4|521|"
assert removed == "3"
