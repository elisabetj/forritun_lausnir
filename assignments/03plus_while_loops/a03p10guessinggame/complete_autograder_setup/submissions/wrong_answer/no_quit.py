hi = 1000
lo = 1

while lo <= hi:
    guess = (lo + hi) // 2
    print(guess)
    cmd = input()
    if cmd == "h":
        hi = guess - 1
    elif cmd == "l":
        lo = guess + 1
    elif cmd == "c":
        print("I AM VICTORIOUS")
        break
    elif cmd == "q":
        break
    else:
        print(f"{cmd} is not among the recognized commands")

if hi < lo:
    print("Tsk, tsk, don't try to cheat me")
