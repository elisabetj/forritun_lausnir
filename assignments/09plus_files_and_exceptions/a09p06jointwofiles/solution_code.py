def main():
    file_name_a = input()
    file_name_b = input()

    file_a = open(file_name_a)
    file_b = open(file_name_b)
    print(join_text_files(file_a, file_b))


def join_text_files(file_a, file_b):
    result = ""
    lines_a = read_all_lines(file_a)
    lines_b = read_all_lines(file_b)

    # We could use the built-in zip() function, but let's do this "by hand"
    max_lines = max(len(lines_a), len(lines_b))
    for line_index in range(max_lines):
        for lines in (lines_a, lines_b):
            line = safe_index(lines, line_index)
            if line is not None:
                result += line + "\n"
    return result.rstrip("\n")  # Get rid of trailing newline


def read_all_lines(text_file):
    text = text_file.read()
    return text.splitlines()


def safe_index(lines, index):
    try:
        return lines[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
