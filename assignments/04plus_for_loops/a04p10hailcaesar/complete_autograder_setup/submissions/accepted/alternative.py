# Read exactly four lines of input
line1 = input()
line2 = input()
line3 = input()
line4 = input()

# Define variables for the range of numbers within which we have 'printable' characters.
# As we shift the input characters, we must ensure that they stay within this range.
HIGH = ord("~")  # 126
LOW = ord(" ")  # 32
BELOW = LOW - 1
LENGTH_OF_RANGE = HIGH - BELOW  # 126 - 31 = 95
# The number of values used is all the values up to 126
# minus all the unused values up to 31

# Every transmission starts with the line "Hail Caesar!"
# so the first letter, once decrypted, must be H.
# Find out what the key is.
first_letter = line1[0]
key = ord(first_letter) - ord("H")

# We can use 'for' to iterate over the lines and decrypt them one by one
for line in (line1, line2, line3, line4):
    decrypted = ""
    for character in line:
        code = ord(character)
        shifted_code = code - key

        # We can use division with remainders
        # to wrap the key around the ends of the range, but to do so,
        # we first need to move the range so that the lower end is 0,
        # then use the modulus, and finally move the range back into place.

        shifted_code = ((shifted_code - LOW) % LENGTH_OF_RANGE) + LOW
        
        # This takes care of values that are below 32,
        # by first moving them down to negative values.
        # And values originally above 126 will now be above 94.
        # The modulus then sends both to the unique equivalent value
        # in the range 0 to LENGTH_OF_RANGE-1 = 95-1 = 94,
        # such that the difference between the original value and the new
        # is a multiple of 95.
        # For example, -1 goes to 94, -2 goes to 93 etc.
        # and 95 goes to 0, 96 goes to 1 etc.
        # Values already in the range 0 to 94 will remain unchanged.
        # Then all that is left is to move the range back up.

        decrypted += chr(shifted_code)
    print(decrypted)
