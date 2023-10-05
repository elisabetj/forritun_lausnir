import sys
import re

tile_regex = "[A-J]([0-9]|10)"

lines = [line.rstrip("\n") for line in sys.stdin.readlines()]

ships = [tuple(ship.split()) for ship in lines[:5]]
attacks = lines[5:]

assert 17 <= len(attacks) <= 100

for ship in ships:
    assert re.search(tile_regex, ship[0])
    assert ship[1] in ("horizontal", "vertical")

for attack in attacks:
    assert re.search(tile_regex, attack)


sys.exit(42)
