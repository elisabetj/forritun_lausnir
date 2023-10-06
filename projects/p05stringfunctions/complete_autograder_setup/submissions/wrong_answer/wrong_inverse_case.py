#!/usr/bin/python3

QUIT = 'q'
COLLECT_DIGITS = 'c'
INVERSE_CASE = 'i'
TO_HEX = 'h'


def collect_digits(a_str):
    '''Returns a string containing all the digits from astr.'''

    digits = ''
    for letter in a_str:
        if letter.isdigit():
            digits += letter
            
    return digits


def inverse_case(a_str):
    '''Returns a string in which upper case letters in a_str are replaced with lower case, and vice versa.'''
    inversed_str = ''
    for char in a_str:
        if char.isdigit():
            continue
        elif char.islower():
            inversed_str += char.upper()
        else:
            inversed_str += char.lower()

    return inversed_str


def to_hex_letter(remainder):
    '''Maps an integer in the range 0-15 to a hexadecimal letter.'''
    if remainder < 10:
        return str(remainder)
    else:
        return chr(remainder + 55)  # A = 65, B = 56, etc.
    

def to_hex(a_int):
    '''Returns a string which is the hexadecimal respresentation of the integer a_int.'''
    if a_int == 0:
        hex_str = '0'
    else:
        hex_str = ''
        quotient = a_int
        while quotient > 0:
            remainder = quotient % 16
            hex_str = to_hex_letter(remainder) + hex_str
            quotient = quotient // 16
        
    return hex_str

    
def main():
    '''Accepts input, calls the appropriate functions, 
    and displays the result.'''
    
    option = input()    
    while option != QUIT:
        a_str = input()
        if option == COLLECT_DIGITS:
            digits = collect_digits(a_str)
            print(digits)      
        elif option == INVERSE_CASE:
            reversed_str = inverse_case(a_str)
            print(reversed_str)
        elif option == TO_HEX:
            an_int = int(a_str)
            hex_str = to_hex(an_int)
            print(hex_str)
            
        option = input()


if __name__ == "__main__":
    main()