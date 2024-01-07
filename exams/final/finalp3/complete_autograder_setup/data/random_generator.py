#!/usr/bin/python3
import random
import sys

OFTEN = 0
NOT_AS_OFTEN = 1

random.seed(int(sys.argv[-1]))

module_name = sys.argv[1]
test_type = sys.argv[2]

def generate_instance(a_tuple):
    """If a_tuple is not None it contains feet and inches from
    some previous call to this method."""

    feet = random.randint(1, 7)
    # In some cases, we want same number of feets as in previous call
    if a_tuple is not None:
        feet_type = random.choices([OFTEN, NOT_AS_OFTEN], [0.8, 0.2])[0]
        if feet_type == NOT_AS_OFTEN:
            feet = a_tuple[0]

    inches_type = random.choices([OFTEN, NOT_AS_OFTEN], [0.8, 0.2])[0]
    if inches_type == OFTEN:
        inches = random.randint(1, 11)
    else:
        inches = random.randint(12, 36)
    print(feet)
    print(inches)

    return(feet, inches)
    

def generate_height():
    print(test_type)
    a_tuple = generate_instance(None)

    if test_type == "__gt__" or test_type == "__add__":
        generate_instance(a_tuple)
    
    
# Main         
print(module_name)
if module_name == "height":
    generate_height()
else:
    assert False, "Invalid module name"
