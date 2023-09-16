name = input()
lastname, firstname = name.split(", ")

print(f"{firstname[0].upper()}. {lastname.capitalize()}")
