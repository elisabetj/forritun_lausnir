#!/usr/bin/python3
import random
import sys

from typing import List
from string import ascii_letters

random.seed(sys.argv[-1])

MIN_NAME_LENGTH = 5
MAX_NAME_LENGTH = 12

def random_name(min_length, max_length):
    first_name_length = random.randint(min_length, max_length)
    last_name_length = random.randint(min_length, max_length)
    first_name = ''.join(random.choice(ascii_letters) for _ in range(first_name_length))
    last_name = ''.join(random.choice(ascii_letters) for _ in range(last_name_length))
    return f"{first_name.capitalize()} {last_name.capitalize()}"

def date_range(year_start, month_start, year_end, month_end) -> List[str]:
    return_range =[]
    for year in range(year_start,year_end+1):
        curr_start_month = 1 if year != year_start else month_start
        curr_end_month = 12 if year != year_end else month_end
        for month in range(curr_start_month, curr_end_month+1):
            return_range.append(f"{year}-{month:02}")
    return return_range

def customer_type_gen(test_type):
    return test_type if test_type != 'mixed' else random.choice(['premium','new','dormant'])

year_start = int(sys.argv[1])
year_end = int(sys.argv[2])
month_start = random.randint(1, 12)
month_end = random.randint(1, 12) if year_start != year_end else random.randint(month_start, 12)
dates = date_range(year_start, month_start, year_end, month_end)

min_customers = int(sys.argv[3])
max_customers = int(sys.argv[4])
customer_amount = random.randint(min_customers, max_customers)
customers = [random_name(MIN_NAME_LENGTH, MAX_NAME_LENGTH) for _ in range(customer_amount)]

test_type = sys.argv[5]

usage_entries = []

for i, customer in enumerate(customers):
    # hopefully will give a good example of premium, new and dormant customers
    customer_type = customer_type_gen(test_type)
    usage = []
    if customer_type == 'premium':
        usage = dates
    elif customer_type == 'new':
        if i == len(customers) - 1:
            #Make one premium customer so the others can be new
            usage = dates  
        else:
            usage = dates[-1:]
    elif customer_type == 'dormant':
        if i == len(customers) - 1:
            #Make one premium customer so the others can be dormant
            usage = dates  
        else:
            times_used = random.randint(1,len(dates))
            usage = random.choices(dates[:-2], k = times_used)
    for entry in usage:
        usage_entries.append(f"{entry},{customer}")
usage_entries.sort()

print(*usage_entries, sep='\n')

