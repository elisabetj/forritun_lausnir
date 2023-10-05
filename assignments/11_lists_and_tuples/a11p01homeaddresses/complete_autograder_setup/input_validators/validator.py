import sys
import re
lines = sys.stdin.readlines()
lines = [x.rstrip() for x in lines]
for line in lines:
    print(line)
    if line != 'q':
        assert(re.search("[a-zA-Zöæð]{3,15} [0-9]{1,4}",line))
    else:
        assert(line == 'q')
exit(42)
