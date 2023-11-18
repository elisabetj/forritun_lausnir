"""A program that prepares to calculate final grades of students in this course.

Takes as input a .csv file exported from the gradebook on a site like Mímir or Coding Rooms.
We need to extract information for every student on how many points they scored
in individual quizzes, assignments, projects and exams,
as well as the maximum available points for each.

Since the semester is not over yet,
it is unknown at this time in which order they will appear in the file.
So this program identifies the columns dynamically
(after the semester is over, it will be possible to simplify this program
by providing this mapping as hard-coded constants).

Then the program prints out the identified indices (nicely formatted),
to show an example of what can be done with the results.
"""

# https://stackoverflow.com/questions/6088581/what-are-python-best-practices-for-dictionary-dict-key-constants
FIRST_NAME = "First name"
LAST_NAME = "Last name"
EMAIL = "Email"
SECTION = "Section"

QUIZZES = "Quizzes"
ASSIGNMENTS = "Assignments"
EXTRA_ASSIGNMENTS = "Extra assignments"
PROJECTS = "Projects"
MIDTERMS = "Midterms"
FINAL_EXAM = "Final exam"
# Feel free to change the values of these constants as you see fit


def main():
    filename = input("Enter filename: ")
    # Implement your solution
    display_results()  # Feel free to change this line


# Feel free to add your own functions of course.


# You can make use of this function, but you need to make some fixes to get the output right.
# Feel free to change it as you see fit (including name and parameters).
def display_results() -> None:
    """Prints out the identified indices along with the corresponding headers."""

    INDENT_ALIGN = 4

    print()

    for attribute in [FIRST_NAME, LAST_NAME, EMAIL, SECTION]:
        index = 0  # Where did you store the index of the column for this attribute?
        label = "How should you describe this attribute?"
        print(f"{index}: {label}")

    for category in [QUIZZES, ASSIGNMENTS, EXTRA_ASSIGNMENTS, PROJECTS, MIDTERMS]:
        header = "What header should go here?"
        print(header)
        for _ in range(1):
            # What do you need to iterate over to find what you're looking for?
            index = 0  # Where did you store the index for this coursework?
            coursework_description = "What should go here?"
            print(f"{index:>{INDENT_ALIGN}}: {coursework_description}")

    what = True
    if what:  # How can you see if the final exam was found in the file?
        index = 0  # Where did you store the index of the column for the final exam?
        label = "What does the header for the final exam look like in the file? Can you look it up?"
        print(f"{index}: {label}")
    else:
        print("The results from the final exam are not in yet.")


if __name__ == "__main__":
    main()
