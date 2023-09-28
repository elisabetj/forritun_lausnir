from solution_code import find_index_of_nth_occurrence

"""
Test case 1:
"""

assert find_index_of_nth_occurrence("321|||", "|", 2) == 4

"""
Test case 2:
"""

assert find_index_of_nth_occurrence("321|||", "|", 4) == -1

"""
Test case 3:
"""

assert find_index_of_nth_occurrence("3|1|2|", "|", 1) == 1

"""
Test case 4:
"""

assert find_index_of_nth_occurrence("3|1|2|", "$", 1) == -1

"""
Test case 5:
"""

assert find_index_of_nth_occurrence("|1|32|", "|", 1) == 0
