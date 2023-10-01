import sys
lines_stripped = [ l.rstrip('\n') for l in sys.stdin.readlines() ]
number_of_people = 0 
for line in lines_stripped:
    if line.isdigit():
        number_of_people = int(line)
        lines_stripped.pop(0)
        break
    lines_stripped.pop(0)

for p in range(number_of_people):
    assert(len(lines_stripped) > 0)
    while not lines_stripped[0].isdigit():
        lines_stripped.pop(0)
exit(42)
