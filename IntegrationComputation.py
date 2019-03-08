# This program will calculate Left and Right hand Riemann Sums, Midpoint Rule,
# and Trapezoidal Rule depending on which you chose and the upper and lower
# bounds, and function given by the user.

import math
import time
import colorama

print ('''
Integration Computation''')
time.sleep(1)

print ('''
This program finds the area under the curve of any function
based on an upper and lower bound given.
''')
time.sleep(2)
method = raw_input('''
What method would you like to use?
        >> ''').lower()
print ("")
running = True

print ('You are going to use the', method, 'method!')

while (running == True):
    running = False