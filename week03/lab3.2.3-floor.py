# This program will take in a float number 
# and outputs an int rounded down.
# Jennifer Ibanez Cano

# we will use the math.floor()

import math

numberTofloor = float(input("Enter a float number: "))
flooredNumber = math.floor(numberTofloor)

print('{} floored is {}'.format(numberTofloor, flooredNumber))