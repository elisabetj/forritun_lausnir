#!/usr/bin/python3

DIGITS = 2   

def main():
    throw_file = input()
    file_stream = open_file(throw_file)
    if file_stream:
        throws_dict = {}
        populate_dict(throws_dict, file_stream)
        file_stream.close()
        print_dict(throws_dict)
        average_tuple = find_highest_average_throw(throws_dict)
        if average_tuple is not None:
            print_highest_average(average_tuple)


def open_file(filename):
    ''' Returns a file stream if filename found, otherwise None '''
    try:
        file_stream = open(filename, "r")
        return file_stream
    except FileNotFoundError:
        return None

    
def populate_dict(throws_dict, file_stream):
    """Populates throws_dict with throws from file_stream 
    Each line in file_stream consists of <first_name last_name throw>.
    """
    for line in file_stream:
        first_name, last_name, throw = line.split()
        throw = float(throw)
        full_name = first_name + " " + last_name
        add_throw_to_dict(throws_dict, full_name, throw)


def add_throw_to_dict(a_dict, name, throw):
    """Adds throw to the list of throws for key name in a_dict."""
    if name in a_dict:
        a_dict[name].append(throw)
    else:
        a_dict[name] = [throw]


def print_dict(a_dict):
    """Prints the information in the given dictionary."""
    for name, throw_list in a_dict.items():
        print('{} Throws: '.format(name), end='')
        print(" ".join([str(throw) for throw in throw_list]))
        

def find_highest_average_throw(a_dict):
    """Returns a tuple (name, throw) for the name with the longest throw.
    Only consider those names that have more than one throw.
    """
    average_tuple = None
    highest_average_throw = 0

    for name, throw_list in a_dict.items():
        if len(throw_list) > 1:
            average_throw = sum(throw_list) / len(throw_list)
            if average_throw > highest_average_throw:
                average_tuple = (name, average_throw)
                highest_average_throw = average_throw

    return average_tuple


def print_highest_average(a_tuple):
    """Prints the name and the throw from a_tuple = (name, score)."""
    (name, throw) = a_tuple
    print('{}: {}'.format(name, round(throw, 2)))


if __name__ == "__main__":
    main()