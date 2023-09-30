#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

command = sys.argv[1]

if command == "1":
    print("random.bin")
elif command == "2":
    print("cancel.bin")
elif command == "3":
    print("empty.bin")
elif command == "4":
    print("doesnotexist.bin")
