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
bound = False

# According to the variables defined above, the area under the curve
# will be calculated here in the correct way using if statements. If
# none of the methods are chosen, it will prompt the user with an
# error message and instructions to correctly initiate the program.

# solves for left hand sums

while (running == True):
    if bound == False and method == 'left hand sums' or method == 'right hand sums' or method == 'trapezoidal rule' or method == 'midpoint rule':
        print colored("You are going to use the"), colored(method, 'green', attrs=['underline']), colored("method! \n")
        equation = raw_input("What is your equation? \n        >> ")  # capture an equation written in terms of f
        f = eval("lambda x: " + equation)  # convert the equation string to an actual lamdba function
        n = float(input("How many sections do you want? \n        >> "))  # takes input for how many sections
        a = float(input("What is your lower bound? \n        >> "))  # takes lower bound
        b = float(input("What is your upper bound? \n        >> "))  # takes upper bound
        dx = float((b - a) / n)  # finds change in x
        s = 0
        a = a + dx
        bound = True
    if method == 'left hand sums':
        while a <= b:   # checks if in x value range
            s = s + f(a) * dx   # calculates sum at each step
            a = a + dx  # adds dx to the lower x value
            print("")
            print (s)
        print colored ("\nThe area under the curve is "), colored(s, 'green', attrs=['underline'])  # states the area under the curve
        running = False

# solves for right hand sums

    elif method == 'right hand sums':
        while b >= a:   # checks if in x value range
            s = s + f(a) * dx   # solves for sum at each step
            a = a + dx  # adds dx to the lower x value
            print (s)
        print colored ("\nThe area under the curve is "), colored(s, 'green', attrs=['underline'])  # states the area under the curve
        running = False

# solves with trapezoidal rule

    elif method == 'trapezoidal rule':
        while a <= b:   # checks if in x value range
            s = s + ((f(a) + f(a + dx) / 2) * dx)   # solves for sum at each step
            a = a + dx  # adds dx to lower x value
            print (s)
        print colored ("\nThe area under the curve is "), colored(s, 'green', attrs=['underline'])  # states the area under the curve
        running = False

# solves with midpoint rule

    elif method == 'midpoint rule':
        while a <= b:   # checks if in x value range
            s = s + (f((a) + (a - dx) / 2) * dx)    # solves for sum at each step
            a = a + dx  # adds dx to lower x value
            print (s)
        print colored ("\nThe area under the curve is "), colored(s, 'green', attrs=['underline'])  # states the area under the curve
        running = False

# displays error message when a method is not chosen

    else:
        method = method.title()
        cprint ("'{}' is not one of the options. Try one of the following methods.".format(method), 'red')
        print ("    - Left Hand Sums \n    - Right Hand Sums \n    - Midpoint Rule \n    - Trapezoidal Rule")
        method = raw_input("\n Which method would you like to use? \n       >> ").lower()
        print ("")