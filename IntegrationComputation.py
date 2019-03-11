# This program will calculate Left and Right hand Riemann Sums, Midpoint Rule,
# and Trapezoidal Rule depending on which you chose and the upper and lower
# bounds, and function given by the user.

import math
import time
from termcolor import cprint
from termcolor import colored

# Startup to code telling the user what the program is capable of doing, as
# well as what they are expected to input

print ("")
cprint ("Integration Computation \n", 'magenta', attrs=['underline', 'bold'])
time.sleep(.5)
print ("This program finds the area under the curve of any function")
time.sleep(.5)
print ("based on an upper and lower bound given. You can use any of")
time.sleep(.5)
print ("the following methods!")
time.sleep(.5)
print ("    - Left Hand Sums")
time.sleep(.5)
print ("    - Right Hand Sums")
time.sleep(.5)
print ("    - Midpoint Rule")
time.sleep(.5)
print ("    - Trapezoidal Rule \n ")
time.sleep(2)
print ("------------------------------------------------------------")
time.sleep(.5)

# Takes users input on the method they want to use, the function they are
# evaluating, the change in x, and the upper and lower bounds.

method = raw_input("\n Which method would you like to use? \n       >> ").lower()
print ("")
running = True

def bound():
    print colored ("You are going to use the"), colored(method, 'green', attrs=['underline']), colored("method! \n")
    equation = raw_input("What is your equation? \n        >> ") # capture an equation written in terms of f
    f = eval("lambda x: " + equation) # convert the equation string to an actual lamdba function
    dx = input("What is your change in x? \n        >> ")
    lower = input("What is your lower bound? \n        >> ")
    upper = input("What is your upper bound? \n        >> ")
    print(f(2))

# According to the variables defined above, the area under the curve
# will be calculated here in the correct way using if statements. If
# none of the methods are chosen, it will prompt the user with an
# error message and instructions to correctly initiate the program.

while (running == True):
    if method == 'left hand sums':
        bound()
    elif method == 'right hand sums':
        bound()
    elif method == 'midpoint rule':
        bound()
    elif method == 'trapezoidal rule':
        bound()
    else:
        method = method.title()
        cprint ("'{}' is not one of the options. Try one of the following methods.".format(method), 'red')
        print ("    - Left Hand Sums \n    - Right Hand Sums \n    - Midpoint Rule \n    - Trapezoidal Rule")
        method = raw_input("\n Which method would you like to use? \n       >> ").lower()
        print ("")