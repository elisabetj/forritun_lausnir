#!/usr/bin/python3

def extract_integers(tokens):
    result = []
    for token in tokens:
        try:
            result.append(int(token))
        except ValueError:
            pass
    return result

def find_missing_integers(integers):
    """
    This is a faster method of finding the missing integers
    Instead of calling `in` to check whether the number is present,
    we can sort the list and add the numbers that fall between the gaps
    This method works quickly even when the numbers and list are large (10^6)
    The method in the solution_code is simpler conceptually,
    but slows down faster as the list and numbers grow in size.
    """
    if not integers:
        return []
    sorted_ints = sorted(integers)
    max_int = sorted_ints[-1]
    missing_ints = []
    counter = 0
    for i in range(len(sorted_ints)):
        while counter < sorted_ints[i]:
            missing_ints.append(counter)
            counter += 1
        # make sure we skip the value in the list
        if counter == sorted_ints[i]:
            counter += 1
    return missing_ints

def main():
    line = input()
    tokens = line.split()
    print(tokens)
    integers = extract_integers(tokens)
    print(integers)
    missing_ints = find_missing_integers(integers)
    print(missing_ints)

if __name__ == "__main__":
    main()
