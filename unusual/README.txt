Log Date : 5th January 2017


Pandigital Number

Pandigital is a number in which if there are n digits,
then the number will contain all digits from 1 to n exactly
once. An example for a 7 pandigital number is 2135467.

Unusual Number

The product 7254 is unusual as the idetity, 39 * 186 = 7254,
containing multiplicand, multiplier and product is 1 through
9 pandigital.

#-----------------------------------------------------------
# ABOUT
#-----------------------------------------------------------
This document includes a basic explantion of the python code
'unusualSum.py', which is used to find the sum of all
unusual products. This document also gives basic
documentation, resoning and explanation to specific section
and functions of the code. This also acts as a log during
the processing of code creation.
#-----------------------------------------------------------
Functions Used
#-----------------------------------------------------------
check_if_pandigital - Checks if passed argument is pandigital
scan - Scans through all values to find unusual product
cli - Main function
#-----------------------------------------------------------

1 * 1000 = 1000
1 * 9999 = 9999
9 * 1111 = 9999
10 * 100 = 1000
99 * 101 = 9999
100 * 10 = 1000

Similarly from calculations we observe that only a 1 X 4 or 
2 X 3 can produce a set of 9 digits. If any of the operands
goes beyond 4 digits, then for sure the product will have 
more than 9 digits. Therefor, in our search we can set the
limits of the operands as 10000, as the largest possible 4
digit value is 9999.

#===========================================================