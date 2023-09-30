from solution_code import rotate_text_clockwise

"""
Test case 1:
"""

original = "Long\nsho"
expected = "sL\nho\non\n g"

rotated = rotate_text_clockwise(original)
assert rotated == expected

"""
Test case 2:
"""

original = "ABC\nDEF\nGHI"
expected = "GDA\nHEB\nIFC"

rotated = rotate_text_clockwise(original)
assert rotated == expected

"""
Test case 3:
"""

original = ""
expected = ""

rotated = rotate_text_clockwise(original)
assert rotated == expected

"""
Test case 4:
"""

original = "single line"
expected = "s\ni\nn\ng\nl\ne\n\nl\ni\nn\ne"

rotated = rotate_text_clockwise(original)
assert rotated == expected
