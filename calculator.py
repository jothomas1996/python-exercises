""" calculator script which can perform addition, substraction, division and multiplication """

import sys

def add(input_1, input_2):
    """ implimentation of addition """
    print input_1 + input_2,

def subtract(input_1, input_2):
    """ implimentation of substraction """
    print input_1 - input_2,

def division(input_1, input_2):
    """ implimentation of division """
    print input_1 / input_2,

def multiply(input_1, input_2):
    """ implimentation of multiplication """
    print input_1 * input_2,

""" system call """

if 'add' in sys.argv[1] :
    add(int(sys.argv[2]), int(sys.argv[3]))
elif 'subtract' in sys.argv[1] :
    subtract(int(sys.argv[2]), int(sys.argv[3]))
elif 'division' in sys.argv[1] :
    division(int(sys.argv[2]), int(sys.argv[3]))
else:
    multiply(int(sys.argv[2]), int(sys.argv[3]))