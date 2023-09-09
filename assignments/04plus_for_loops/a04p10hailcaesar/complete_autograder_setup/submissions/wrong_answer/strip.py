line1 = input()
line2 = input()
line3 = input()
line4 = input()

HIGH = ord("~")  # 126
LOW = ord(" ")  # 32
BELOW = LOW - 1
LENGTH_OF_RANGE = HIGH - BELOW  # 126 - 31 = 95

first_letter = line1[0]
key = ord(first_letter) - ord("H")

for line in (line1, line2, line3, line4):
    decrypted = ""
    for character in line:
        code = ord(character)
        shifted_code = code - key
        shifted_code = ((shifted_code - LOW) % LENGTH_OF_RANGE) + LOW
        decrypted += chr(shifted_code)

    # This line is incorrect
    print(decrypted.strip())
