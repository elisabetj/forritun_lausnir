def main():
    file_name = input()

    try:
        with open(file_name) as file:
            print_reversed_words(file_obj=file)

    except FileNotFoundError:
        print(f"File {file_name} not found.")


def print_reversed_words(file_obj):
    for line in file_obj:
        line = line.strip()

        for word in line.split():
            print(word[::-1], end=" ")

        print()


if __name__ == "__main__":
    main()
