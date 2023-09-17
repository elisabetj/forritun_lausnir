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
if key < 0:
    key += LENGTH_OF_RANGE

# We can use 'for' to iterate over the lines and decrypt them one by one.
for line in (line1, line2, line3, line4):
    decrypted = ""
    for character in line:
        code = ord(character)
        shifted_code = code - key
        if shifted_code < LOW:
            shifted_code += LENGTH_OF_RANGE

        decrypted += chr(shifted_code)

    print(decrypted)
