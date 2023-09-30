from solution_code import change_indentation

"""
Unit tests:

Test case 1:
test_increase_indentation
"""

original = "print(x)\ny = input()\n"
expected = "    print(x)\n    y = input()\n"
actual = change_indentation(original, 4)
assert actual == expected

"""
Test case 2:
test_decrease_indentation
"""

original = "    print(x)\n    y = input()\n"
expected = "  print(x)\n  y = input()\n"
actual = change_indentation(original, -2)
assert actual == expected

"""
Test case 3:
test_decrease_beyond_limit
"""

original = "    print(x)\n    y = input()\n"
expected = "print(x)\ny = input()\n"
actual = change_indentation(original, -6)
assert actual == expected

"""
Test case 4:
test_increase_beyond_limit
"""

original = "print(x)".rjust(68) + "\n" + "y = input()".rjust(68) + "\n"
expected = "print(x)".rjust(70) + "\n" + "y = input()".rjust(70) + "\n"
actual = change_indentation(original, 4)
assert actual == expected


"""
Test case 5:
test_do_nothing
"""

original = "print(x)".rjust(68) + "\n" + "y = input()".rjust(68) + "\n"
actual = change_indentation(original, 0)
assert actual == original
