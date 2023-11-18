"""
I/O tests:

Test case 1 (1. Invalid guess):
Points: 2

Input:
yby
yrgby
xrgr
r g r g
yyby
n

Output:
Welcome to Mastermind.
The codemaker has selected a code.
The code is a sequence of four colors. It may contain duplicates.
There are 6 possible colors to choose from:
 - (r)ed
 - (g)reen
 - (b)lue
 - (y)ellow
 - (p)urple
 - (o)range
It's your job to break the code by making a series of guesses.
Each guess consists of four letters corresponding to the colors listed above.
Example: to guess red, green, blue and orange, type rgbo and press Enter.

------------------------    The game starts now    -----------------------------
You have 8 guesses left. What's your guess?
That's not a valid guess.
Please enter four letters from an alphabet of rgbypo
You have 8 guesses left. What's your guess?
That's not a valid guess.
Please enter four letters from an alphabet of rgbypo
You have 8 guesses left. What's your guess?
That's not a valid guess.
Please enter four letters from an alphabet of rgbypo
You have 8 guesses left. What's your guess?
That's not a valid guess.
Please enter four letters from an alphabet of rgbypo
You have 8 guesses left. What's your guess?
Congratulations, you have guessed the code!
Would you like to play again (y/n)? 


Test case 2 (2. Loss):
Points: 3

Input:
oopp
popo
ogry
yoyo
rbgy
brop
grob
obbo
n

Output:
Welcome to Mastermind.
The codemaker has selected a code.
The code is a sequence of four colors. It may contain duplicates.
There are 6 possible colors to choose from:
 - (r)ed
 - (g)reen
 - (b)lue
 - (y)ellow
 - (p)urple
 - (o)range
It's your job to break the code by making a series of guesses.
Each guess consists of four letters corresponding to the colors listed above.
Example: to guess red, green, blue and orange, type rgbo and press Enter.

------------------------    The game starts now    -----------------------------
You have 8 guesses left. What's your guess?
Elements with the correct color and position:                                  0
Elements with the correct color but incorrect position:                        0
You have 7 guesses left. What's your guess?
Elements with the correct color and position:                                  0
Elements with the correct color but incorrect position:                        0
You have 6 guesses left. What's your guess?
Elements with the correct color and position:                                  1
Elements with the correct color but incorrect position:                        0
You have 5 guesses left. What's your guess?
Elements with the correct color and position:                                  1
Elements with the correct color but incorrect position:                        1
You have 4 guesses left. What's your guess?
Elements with the correct color and position:                                  1
Elements with the correct color but incorrect position:                        1
You have 3 guesses left. What's your guess?
Elements with the correct color and position:                                  0
Elements with the correct color but incorrect position:                        1
You have 2 guesses left. What's your guess?
Elements with the correct color and position:                                  0
Elements with the correct color but incorrect position:                        1
You have 1 guesses left. What's your guess?
Elements with the correct color and position:                                  1
Elements with the correct color but incorrect position:                        0
You failed to guess yyby. Game over :(
Would you like to play again (y/n)? 


Test case 3 (3. Play again):
Points: 2

Input:
ybyy
yyby
y
rpop
rpyp
rpbp
n

Output:
Welcome to Mastermind.
The codemaker has selected a code.
The code is a sequence of four colors. It may contain duplicates.
There are 6 possible colors to choose from:
 - (r)ed
 - (g)reen
 - (b)lue
 - (y)ellow
 - (p)urple
 - (o)range
It's your job to break the code by making a series of guesses.
Each guess consists of four letters corresponding to the colors listed above.
Example: to guess red, green, blue and orange, type rgbo and press Enter.

------------------------    The game starts now    -----------------------------
You have 8 guesses left. What's your guess?
Elements with the correct color and position:                                  2
Elements with the correct color but incorrect position:                        2
You have 7 guesses left. What's your guess?
Congratulations, you have guessed the code!
Would you like to play again (y/n)?
------------------------    The game starts now    -----------------------------
You have 8 guesses left. What's your guess?
Elements with the correct color and position:                                  3
Elements with the correct color but incorrect position:                        0
You have 7 guesses left. What's your guess?
Elements with the correct color and position:                                  3
Elements with the correct color but incorrect position:                        0
You have 6 guesses left. What's your guess?
Congratulations, you have guessed the code!
Would you like to play again (y/n)? 


Test case 4 (4. Win):
Points: 3

Input:
rrgg
yybb
yyyb
yyby
n

Output:
Welcome to Mastermind.
The codemaker has selected a code.
The code is a sequence of four colors. It may contain duplicates.
There are 6 possible colors to choose from:
 - (r)ed
 - (g)reen
 - (b)lue
 - (y)ellow
 - (p)urple
 - (o)range
It's your job to break the code by making a series of guesses.
Each guess consists of four letters corresponding to the colors listed above.
Example: to guess red, green, blue and orange, type rgbo and press Enter.

------------------------    The game starts now    -----------------------------
You have 8 guesses left. What's your guess?
Elements with the correct color and position:                                  0
Elements with the correct color but incorrect position:                        0
You have 7 guesses left. What's your guess?
Elements with the correct color and position:                                  3
Elements with the correct color but incorrect position:                        0
You have 6 guesses left. What's your guess?
Elements with the correct color and position:                                  2
Elements with the correct color but incorrect position:                        2
You have 5 guesses left. What's your guess?
Congratulations, you have guessed the code!
Would you like to play again (y/n)? 
"""
