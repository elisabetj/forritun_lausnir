HIGH = ord("~")  # 126
LOW = ord(" ")  # 32
BELOW = LOW - 1
LENGTH_OF_RANGE = HIGH - BELOW  # 126 - 31 = 95

lines = [input() for _ in range(4)]

first_letter = lines[0][0]
key = ord(first_letter) - ord("H")

for line in lines:
    decrypted = ""
    for character in line:
        code = ord(character)
        shifted_code = ((code - key - LOW) % LENGTH_OF_RANGE) + LOW
        decrypted += chr(shifted_code)

    print(decrypted)
