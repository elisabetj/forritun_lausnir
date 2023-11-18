import sys
import re

SIDE_SEPARATOR = " <=> "
FORMULA_SEPARATOR = " + "
FORMULA_SEARCH_STRING = "([A-Z][a-z]?[0-9]{0,2}){1,10}"

chemical_equation = ''.join(sys.stdin.readlines())

left_side, right_side = chemical_equation.split(SIDE_SEPARATOR)

left_side_formulae = left_side.split(FORMULA_SEPARATOR)
right_side_formulae = right_side.split(FORMULA_SEPARATOR)

assert (len(left_side_formulae) + len(right_side_formulae)) <= 100, "Too many formulae"

for formula in left_side_formulae:
    assert re.search(FORMULA_SEARCH_STRING, formula), "Format of formulas incorrect"

for formula in right_side_formulae:
    assert re.search(FORMULA_SEARCH_STRING, formula), "Format of formulas incorrect"

assert not sys.stdin.read()

sys.exit(42)
