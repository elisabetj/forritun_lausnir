#!/usr/bin/python3

SPECIAL_TOKENS = ".,!?"

def print_list(the_list):
    print(len(the_list))
    print('\n'.join(the_list))
    
def tokenize(words):
    tokens = []
    for word in words:
        if word[-1] in SPECIAL_TOKENS:
            tokens.append(word[:-1])
            tokens.append(word[-1])
        else:
            tokens.append(word)
    return tokens

def main():
    filename = input()

    try:
        with open(filename) as f:
            words = f.read().split()
            tokens = tokenize(words)
            print_list(words)
            print_list(tokens)
    except OSError:
        pass


if __name__ == "__main__":
    main()
