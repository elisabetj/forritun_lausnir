email_address = input()

local_part, at_symbol, domain = email_address.partition("@")

if at_symbol != "@":
    print("@ symbol is missing.")
elif "@" in domain:
    index = email_address.find("@", len(local_part) + 1)
    padding = " " * index
    print(email_address)
    print(padding + "^--there is an extra @ symbol here.")
elif len(local_part) == 0:
    print("There is nothing before the @ symbol.")
elif len(domain) == 0:
    padding = " " * len(email_address)
    print(email_address)
    print(padding + "^--there is nothing after the @ symbol.")
elif local_part.startswith("."):
    print("Email address starts with a dot.")
elif local_part.endswith("."):
    padding = " " * (len(local_part) - 1)
    print(email_address)
    print(padding + "^--there is an extra dot here.")
elif ".." in email_address:
    start_index = email_address.find("..")
    padding = " " * start_index
    print(email_address)
    print(padding + "^--there are consecutive dots here.")
elif "." not in domain:
    print("Top-level-domain is missing.")
else:
    print("All good.")
