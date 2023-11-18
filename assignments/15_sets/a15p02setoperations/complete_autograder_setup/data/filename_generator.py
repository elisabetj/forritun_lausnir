#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1]) 

filename1_suffix = int(sys.argv[1]) 
filename2_suffix = filename1_suffix + 1

filename1 = f"test_file_{filename1_suffix:02d}.txt"
filename2 = f"test_file_{filename2_suffix:02d}.txt"

print(filename1)
print(filename2)
