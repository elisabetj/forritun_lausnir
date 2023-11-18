"""
I/O tests:

Test case 1 (1. File not found):

Input:
unicorn.csv

Output:
Enter filename: File 'unicorn.csv' not found.


Test case 2 (2. Before final exam):
Description: Final exam not included in file

Input:
Muggle Studies 2021-3 (T-111-MUST) standard grades.csv

Output:
Enter filename: 
Individual quizzes:
  50.0 points possible for Quiz 0 (Individual): Introduction
  45.0 points possible for Quiz 1 (Individual): Basics
  50.0 points possible for Quiz 2 (Individual): Decisions and booleans
  50.0 points possible for Quiz 3 (Individual): While loops
  50.0 points possible for Quiz 4 (Individual): For loops
  50.0 points possible for Quiz 5 (Individual): Algorithms and git
  50.0 points possible for Quiz 6 (Individual): Strings
  45.0 points possible for Quiz 7 (Individual): Functions
  50.0 points possible for Quiz 8 (Individual): Functions
  30.0 points possible for Quiz 9 (Individual): Files and exceptions
  45.0 points possible for Quiz 10 (Individual): Lists
  50.0 points possible for Quiz 11 (Individual): Lists and tuples
  50.0 points possible for Quiz 12 (Individual): More on functions
  50.0 points possible for Quiz 13 (Individual): Dictionaries
  50.0 points possible for Quiz 14 (Individual): Sets and scope
Group quizzes:
  50.0 points possible for Quiz 0 (Group): Introduction
  45.0 points possible for Quiz 1 (Group): Basics
  50.0 points possible for Quiz 2 (Group): Decisions and booleans
  50.0 points possible for Quiz 3 (Group): While loops
  50.0 points possible for Quiz 4 (Group): For loops
  50.0 points possible for Quiz 5 (Group): Algorithms and git
  50.0 points possible for Quiz 6 (Group): Strings
  45.0 points possible for Quiz 7 (Group): Functions
  50.0 points possible for Quiz 8 (Group): Functions
  30.0 points possible for Quiz 9 (Group): Files and exceptions
  45.0 points possible for Quiz 10 (Group): Lists
  50.0 points possible for Quiz 11 (Group): Lists and tuples
  50.0 points possible for Quiz 12 (Group): More on functions
  50.0 points possible for Quiz 13 (Group): Dictionaries
  50.0 points possible for Quiz 14 (Group): Sets and scope
Assignments:
  30.0 points possible for Assignment 1: Basics
  30.0 points possible for Assignment 2: Decisions and Booleans
  30.0 points possible for Assignment 3: While loops
  30.0 points possible for Assignment 4: For loops
  10.0 points possible for Assignment 5: Algorithms and git
  30.0 points possible for Assignment 6: Strings
  25.0 points possible for Assignment 7: Functions
   5.0 points possible for Assignment 8: TileTraveller
  25.0 points possible for Assignment 9: Files and Exceptions
  22.0 points possible for Assignment 10: Lists
  25.0 points possible for Assignment 11: Lists and tuples
  25.0 points possible for Assignment 12: More on functions
  17.0 points possible for Assignment 13: TileTraveller2
  25.0 points possible for Assignment 14: Dictionaries
  15.0 points possible for Assignment 15: Sets
Extra assignments:
  24.0 points possible for Assignment 1+: More basics
  16.0 points possible for Assignment 2+: Decisions and booleans
  18.0 points possible for Assignment 3+: While loops
  15.0 points possible for Assignment 4+: For loops
  10.0 points possible for Assignment 5+: Algorithms
  14.0 points possible for Assignment 6+: Strings
  30.0 points possible for Assignment 7+: Functions
  15.0 points possible for Assignment 8+: Functions for homework and fun
  10.0 points possible for Assignment 9+: Files and Exceptions
  10.0 points possible for Assignment 10+: Lists
   5.0 points possible for Assignment 11+: Lists and tuples
   5.0 points possible for Assignment 12+: Snakes and Ladders
   9.0 points possible for Assignment 13+: Functions return
   5.0 points possible for Assignment 14+: Dictionaries
   5.0 points possible for Assignment 15+: Customer Analytics
Projects:
  10.0 points possible for Project 1: BMI
  10.0 points possible for Project 2: Commission
  20.0 points possible for Project 3: Mult and harmonic
  20.0 points possible for Project 4: Calculator
  20.0 points possible for Project 5: Hex and Decimal
  20.0 points possible for Project 6: Data Processing
  20.0 points possible for Project 7: Grades
  20.0 points possible for Project 8: Airline Seating
  10.0 points possible for Project 9: Word classes
Midterms:
  40.0 points possible for Midterm 1
  80.0 points possible for Midterm 2
The number of possible points on the final exam is not available yet.


Test case 3 (3. After final exam):
Description: Final exam included in file

Input:
Muggle Studies 2021-3 (T-111-MUST) standard grades - with final exam included.csv

Output:
Enter filename: 
Individual quizzes:
  50.0 points possible for Quiz 0 (Individual): Introduction
  45.0 points possible for Quiz 1 (Individual): Basics
  50.0 points possible for Quiz 2 (Individual): Decisions and booleans
  50.0 points possible for Quiz 3 (Individual): While loops
  50.0 points possible for Quiz 4 (Individual): For loops
  50.0 points possible for Quiz 5 (Individual): Algorithms and git
  50.0 points possible for Quiz 6 (Individual): Strings
  45.0 points possible for Quiz 7 (Individual): Functions
  50.0 points possible for Quiz 8 (Individual): Functions
  30.0 points possible for Quiz 9 (Individual): Files and exceptions
  45.0 points possible for Quiz 10 (Individual): Lists
  50.0 points possible for Quiz 11 (Individual): Lists and tuples
  50.0 points possible for Quiz 12 (Individual): More on functions
  50.0 points possible for Quiz 13 (Individual): Dictionaries
  50.0 points possible for Quiz 14 (Individual): Sets and scope
Group quizzes:
  50.0 points possible for Quiz 0 (Group): Introduction
  45.0 points possible for Quiz 1 (Group): Basics
  50.0 points possible for Quiz 2 (Group): Decisions and booleans
  50.0 points possible for Quiz 3 (Group): While loops
  50.0 points possible for Quiz 4 (Group): For loops
  50.0 points possible for Quiz 5 (Group): Algorithms and git
  50.0 points possible for Quiz 6 (Group): Strings
  45.0 points possible for Quiz 7 (Group): Functions
  50.0 points possible for Quiz 8 (Group): Functions
  30.0 points possible for Quiz 9 (Group): Files and exceptions
  45.0 points possible for Quiz 10 (Group): Lists
  50.0 points possible for Quiz 11 (Group): Lists and tuples
  50.0 points possible for Quiz 12 (Group): More on functions
  50.0 points possible for Quiz 13 (Group): Dictionaries
  50.0 points possible for Quiz 14 (Group): Sets and scope
Assignments:
  30.0 points possible for Assignment 1: Basics
  30.0 points possible for Assignment 2: Decisions and Booleans
  30.0 points possible for Assignment 3: While loops
  30.0 points possible for Assignment 4: For loops
  10.0 points possible for Assignment 5: Algorithms and git
  30.0 points possible for Assignment 6: Strings
  25.0 points possible for Assignment 7: Functions
   5.0 points possible for Assignment 8: TileTraveller
  25.0 points possible for Assignment 9: Files and Exceptions
  22.0 points possible for Assignment 10: Lists
  25.0 points possible for Assignment 11: Lists and tuples
  25.0 points possible for Assignment 12: More on functions
  17.0 points possible for Assignment 13: TileTraveller2
  25.0 points possible for Assignment 14: Dictionaries
  15.0 points possible for Assignment 15: Sets
Extra assignments:
  24.0 points possible for Assignment 1+: More basics
  16.0 points possible for Assignment 2+: Decisions and booleans
  18.0 points possible for Assignment 3+: While loops
  15.0 points possible for Assignment 4+: For loops
  10.0 points possible for Assignment 5+: Algorithms
  14.0 points possible for Assignment 6+: Strings
  30.0 points possible for Assignment 7+: Functions
  15.0 points possible for Assignment 8+: Functions for homework and fun
  10.0 points possible for Assignment 9+: Files and Exceptions
  10.0 points possible for Assignment 10+: Lists
   5.0 points possible for Assignment 11+: Lists and tuples
   5.0 points possible for Assignment 12+: Snakes and Ladders
   9.0 points possible for Assignment 13+: Functions return
   5.0 points possible for Assignment 14+: Dictionaries
   5.0 points possible for Assignment 15+: Customer Analytics
Projects:
  10.0 points possible for Project 1: BMI
  10.0 points possible for Project 2: Commission
  20.0 points possible for Project 3: Mult and harmonic
  20.0 points possible for Project 4: Calculator
  20.0 points possible for Project 5: Hex and Decimal
  20.0 points possible for Project 6: Data Processing
  20.0 points possible for Project 7: Grades
  20.0 points possible for Project 8: Airline Seating
  10.0 points possible for Project 9: Word classes
Midterms:
  40.0 points possible for Midterm 1
  80.0 points possible for Midterm 2
10.0 points possible for Final
"""
