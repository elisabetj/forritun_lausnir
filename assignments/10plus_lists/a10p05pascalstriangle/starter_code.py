def main():
    # Main program - DO NOT CHANGE
    height = int(input())
    new_row = []
    for _ in range(height):
        new_row = make_new_row(new_row)
        print(new_row)


# Implement any functions you need.


if __name__ == "__main__":
    main
