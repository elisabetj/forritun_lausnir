text_to_translate = input()

# The solution supports uppercase inputs but it is unnecessary.
VOWELS = "aeiouyAEIOUY"
translation = ""

for word in text_to_translate.split():
    vowel_index = -1
    for index, character in enumerate(word):
        if character in VOWELS:
            vowel_index = index
            break

    if vowel_index == -1:
        translated_word = word + "ay"
    elif vowel_index == 0:
        translated_word = word + "yay"
    else:
        assert vowel_index > 0
        initial_consonants = word[:vowel_index]
        rest = word[vowel_index:]
        translated_word = rest + initial_consonants + "ay"

    translation += translated_word + " "

translation = translation.strip()  # Get rid of trailing whitespace.
print(translation)
