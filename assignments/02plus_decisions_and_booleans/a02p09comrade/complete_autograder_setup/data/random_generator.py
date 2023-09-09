#!/usr/bin/python3
import random
import sys

random.seed(sys.argv[-1])

tp = sys.argv[1]

a_dict = {"shutdown": (350, 400),
          "raise": (0, 299),
          "lower": (301, 349),
          "keep_low": (1, 299),
          "keep": (300, 300),
          "keep_high": (301, 348)}
min_a, max_a = a_dict[tp]
a = random.randint(min_a, max_a)

b_dict = {"shutdown": (0, 349),
          "raise": (a, 349),
          "lower": (0, a),
          "keep_low": (0, a-1),
          "keep": (0, 349),
          "keep_high": (a+1, 349)}
min_b, max_b = b_dict[tp]

b = random.randint(min_b, max_b)
print(a)
print(b)
