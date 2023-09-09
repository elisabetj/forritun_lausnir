rating = int(input())

if rating < 1000:
    print("invalid")
elif rating < 2400:
    print("amateur")
elif rating < 2500:
    print("international   grandmaster")
elif rating < 2700:
    print("grandmaster     ")
else:
    print("super        grandmaster")
