def main():
    # TODO: Write the main program.
    raise NotImplementedError  # TODO: Remove this line when you're done.


# You can use this function if you like.
def open_file(filename):
    """Opens the file with the given file name.

    Returns the corresponding file stream, or None if the file cannot be opened.
    """

    try:
        file_stream = open(filename)
        return file_stream
    except FileNotFoundError:
        return None


# Feel free to define more functions of course.

if __name__ == "__main__":
    main()
