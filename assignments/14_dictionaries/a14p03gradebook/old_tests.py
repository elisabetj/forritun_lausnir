"""
I/O tests:

Test case 1:

Input:
JohnD@ru.is
3
y
JohnD@ru.is
10
y
JohnD@ru.is
7
y
MaryC@ru.is
9
y
MaryC@ru.is
8
n

Output:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
JohnD@ru.is: 6.67
MaryC@ru.is: 8.5


Test case 2:
Description: Only one grade per student.

Input:
student1@ru.is
10
y
student2@ru.is
5
y
student3@ru.is
1
n

Output:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
student1@ru.is: 10.0
student2@ru.is: 5.0
student3@ru.is: 1.0


Test case 3:
Description: Single grade, single student.

Input:
student1@ru.is
2
n

Output:
Enter the student email:
Enter the students grade:
Would you like to add another grade (y/n)?:
student1@ru.is: 2.0
"""
