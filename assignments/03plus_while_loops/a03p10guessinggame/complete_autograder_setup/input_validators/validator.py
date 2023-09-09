import sys
hi = 1000
lo = 1

while lo <= hi:
    guess = (lo + hi) // 2
    cmd = sys.stdin.readline()
    assert cmd in ['l\n', 'h\n', 'c\n', 'q\n']
    cmd = cmd[0]
    if cmd == "h":
        hi = guess - 1
    elif cmd == "l":
        lo = guess + 1
    elif cmd == "c":
        break
    elif cmd == "q":
        break

assert sys.stdin.read() == ''
sys.exit(42)
