edit: i just noticed that i kept typing "binom" instead of "binomial" for some reason.

This is a program created for the purpose of trying to visualize the Newton's Binom.
The Input takes two factors and the power of the binow, each separated by a space.
The factors can be either a number (ex. "53"), one letter ("b"), a product of a number and a letter ("2b"), or a letter taken to a numeric power ("2b^3")
The Output begins with a rewritten version of the Input consisting of 2 lists (each containing the number, letter (if given) and power of the corresponding factor) and the power of the binom. The calculated binom is the end of the Output.

Ex #1
Input: 
2 3 4
Output:
[2, '', 1] [3, '', 1] 4
16 + 96 + 216 + 216 + 81

Ex #2
Input: 
2a b 4
Output:
[2, 'a', 1] [1, 'b', 1] 4
16*a^4 + 32*a^3*b + 24*a^2*b^2 + 8*a*b^3 + b^4

Ex #3
Input: 
4x^3 3y^2 2
Output:
[4, 'x', '3'] [3, 'y', '2'] 2
16*x^6 + 24*x^3*y^2 + 9*y^4
