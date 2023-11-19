import re
import sys

def main():
    line = sys.stdin.readline()
    assert re.match("^[a-zA-Z0-9._-]+\n$", line)
    
    filename = line.rstrip('\n')
    if filename not in ["movies-top-20.csv", "movies-top-250.csv"]:
        assert not sys.stdin.read(), "Trailing input"
        exit(42)

    while True:
        line = sys.stdin.readline()
        assert re.match("^[a-zA-Z0-9]+\n$", line), "Operation ill formed"
        op = line.strip()
        if op == "1":
            pass
        elif op == "2":
            line = sys.stdin.readline()
            assert re.match("^[1-9][0-9]*\n$", line), "Year ill formed"
            year = int(line)
            assert 1900 <= year <= 2023, "Year out of range"
        elif op == "3":
            line = sys.stdin.readline()
            assert line.endswith('\n')
            try:
                value = line.rstrip('\n')
                assert str(float(value)) == value, "Ill formed float"
                assert -10.0 <= float(value) <= 10.0, "Value out of range"
            except:
                assert False, "Could not parse float"
        else:
            break

    assert not sys.stdin.read(), "Trailing input"
    exit(42)


if __name__ == "__main__":
    main()
