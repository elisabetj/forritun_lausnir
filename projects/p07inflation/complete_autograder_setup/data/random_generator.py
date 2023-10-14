#!/usr/bin/python3

import random
import sys
import string

def get_data(file_object):

    '''Returns a list of tuples found in each line in the given file_oject.
    Each tuple is of the form (year_month, index)''' 
    
    tuple_list = []
    for line in file_object:
        (year_month_str, index_str) = line.split()
        tuple_list.append((year_month_str, index_str)) 	
    return tuple_list


filename_number = int(sys.argv[1])
filename = "test"+str(filename_number)+".txt"
random.seed(filename_number)

start_line = random.randint(1, 425) # 425 lines in data.txt
end_line = random.randint(start_line, 425)

file_object = open("data.txt", 'r')
tuple_list = get_data(file_object)


with open(filename, 'w+') as f:
    for i in range(start_line, end_line):
        f.write(tuple_list[i][0] + " " + tuple_list[i][1] + "\n")
