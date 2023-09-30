#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

command = sys.argv[1]

if command == "aa":
    print("a.txt")
    print("a.txt")
elif command == "ac":
    print("a.txt")
    print("c.txt")
elif command == "ba":
    print("b.txt")
    print("a.txt")
elif command == "bb":
    print("b.txt")
    print("b.txt")
elif command == "bc":
    print("b.txt")
    print("c.txt")
elif command == "cb":
    print("c.txt")
    print("b.txt")
elif command == "cc":
    print("c.txt")
    print("c.txt")