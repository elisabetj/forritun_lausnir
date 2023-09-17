n = int(input())

if n == 1:
    no_evidence_to_the_contrary_found = False
else:
    no_evidence_to_the_contrary_found = True

potential_factor = 2
while potential_factor**2 <= n and no_evidence_to_the_contrary_found:
    if n % potential_factor == 0:
        no_evidence_to_the_contrary_found = False

    potential_factor += 1

if no_evidence_to_the_contrary_found:
    print("prime")
else:
    print("not prime")
