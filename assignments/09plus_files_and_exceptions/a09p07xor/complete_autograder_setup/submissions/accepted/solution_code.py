EMPTY_BYTE = b""


def main():
    file_name = input()
    try:
        file = open(file_name, "rb")
        checksum = calculate_xor_checksum(file)
        file.close()

        print(f"The checksum is x{checksum:02x}")

    except FileNotFoundError:
        print("No file named", file_name, "could be found")


def calculate_xor_checksum(binary_file):
    """Calculates a byte-wise XOR checksum for a file, opened in binary mode."""

    checksum = 0
    while (byte := binary_file.read(1)) != EMPTY_BYTE:
        checksum ^= byte[0]

    return checksum


if __name__ == "__main__":
    main()
