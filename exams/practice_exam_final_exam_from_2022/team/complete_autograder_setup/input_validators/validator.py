import sys

MAX_LENGTH_OF_LINE = 10

TEST_TYPES = [
    "Player.__init__",
    "Player.__str__",
    "Player.add_goals",
    "Team.__init__",
    "Team.__str__",
    "Team.__add__",
    "Team.add_player",
    "Team.most_goals_player",
]


def main():
    lines = sys.stdin.readlines()

    for line in lines:
        assert line.endswith("\n") and not line.endswith("\n\n")
        line = line.rstrip("\n")
        assert line == line.rstrip()
        if line.isnumeric() and line.startswith("0"):
            assert line == "0"

    assert len(lines) >= 1
    first_line = lines[0].rstrip("\n")
    assert first_line in TEST_TYPES, f"Unexpected test type encountered: {first_line}"

    for line in lines[1:]:
        line = line.rstrip("\n")
        assert len(line) <= MAX_LENGTH_OF_LINE, f"{line}\n{len(line)}"

    last_line = lines[-1]
    assert last_line.strip()

    exit(42)


if __name__ == "__main__":
    main()
