import sys

# math tan, time.sleep, random.randint, threading.enumerate, collections.namedtuple, math.cos, print
function_list = [
    "tan",
    "sleep",
    "randint",
    "enumerate",
    "namedtuple",
    "cos",
    "important_function1",
    "new_line",
]

print(function_list[int(sys.argv[1]) - 1])
