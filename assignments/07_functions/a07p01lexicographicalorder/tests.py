from solution_code import precedes

"""
Test case 1:
"""

result = precedes("monkey", "cat")
print(result)
assert result == "cat"

"""
Test case 2:
"""

result = precedes("muna", "gleyma")
print(result)
assert result == "gleyma"

"""
Test case 3:
"""

result = precedes("cat", "bat")
print(result)
assert result == "bat"

"""
Test case 4:
Points: 2
"""

result = precedes("Programming", "forritun")
print(result)
assert result == "forritun"
