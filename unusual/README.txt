#===========================================================
Log Date : 6th January 2017
#===========================================================

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
Log Date : 7th January 2017
#===========================================================

ERROR :::: The code is running fine, but when run with small
search space limits like 200, I obtain a set of solutions 
starting with, 27 * 198 = 5346. But when running with larger
limits such as 1000, I obtain more results such as 12 * 483 
= 5796, which is supposed to occur before 27 * 198.
[NOT RESOLVED]

#===========================================================
Log Date : 8th January 2017
#===========================================================

The running time of the code is too long. The only way to 
reduce the running time is to reduce the search space of 
the code. Currently the code goes through all calculations 
from 0 * 0 to 9999 * 9999.

Method 1 : Remove redundant calculations
45 * 25 and 25 * 45 gives the same results, and there are
many such calculations in our search space. These reduntant
calculations are removed using a list 'checked' where the
multiplicand and multiplier of all completed calculations
are stored as a set. Every time a new calculation occurs,
we check the list to ensure that this calcculation has not
has not aldready been performed in the past.
--> set([45,25]) is equal to set([25,45])

#===========================================================