email_address = input()

local_part, at_symbol, domain = email_address.partition("@")

if at_symbol != "@":
    print("@ symbol is missing.")
elif len(local_part) == 0:
    print("There is nothing before the @ symbol.")
elif local_part.startswith("."):
    print("Email address starts with a dot.")
elif local_part.endswith("."):
    print("^--there is an extra dot here.")
elif ".." in email_address:
    print("^--there are consecutive dots here.")
elif len(domain) == 0:
    print("^--there is nothing after the @ symbol.")
elif "@" in domain:
    print("^--there is an extra @ symbol here.")
elif "." not in domain:
    print("Top-level-domain is missing.")
else:
    print("All good.")
