a_str = input()

new_str = ""
for char in a_str:
    if char.islower():
        new_str += char.upper()
    else:
        new_str += char.lower()

print(new_str)
