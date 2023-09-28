from solution_code import put_on_pillar

"""
Unit tests:

Test case 1:
Points: 2
"""

state = "3|2||"
disc = "1"
pillar = 2
new_state = put_on_pillar(state, disc, pillar)
assert new_state == "3|21||"

"""
Test case 2:
Points: 2
"""

state = "3||1|"
disc = "2"
pillar = 2
new_state = put_on_pillar(state, disc, pillar)
assert state == "3|2|1|"

"""
Test case 3:
Points: 1
"""

state = "|4|521|"
disc = "3"
pillar = 1
new_state = put_on_pillar(state, disc, pillar)
assert state == "3|4|521|"
