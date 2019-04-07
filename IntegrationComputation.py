# This program will calculate Left and Right hand Riemann Sums, Midpoint Rule,
# and Trapezoidal Rule depending on which you chose and the upper and lower
# bounds, and function given by the user.

from math import *
import time
from termcolor import cprint
from termcolor import colored

# Startup to code telling the user what the program is capable of doing, as
# well as what they are expected to input

print ("")
cprint ("Integration Computation \n", 'magenta', attrs=['underline', 'bold'])
print ("This program finds the area under the curve of any function")
print ("based on an upper and lower bound given. You can use any of")
print ("the following methods!")
print ("    - Left Hand Sums")
print ("    - Right Hand Sums")
print ("    - Midpoint Rule")
print ("    - Trapezoidal Rule")
print ("    - All \n ")
print ("------------------------------------------------------------")

# Takes users input on the method they want to use, the function they are
# evaluating, the change in x, and the upper and lower bounds.

method = raw_input("\n Which method would you like to use? \n       >> ").lower()
print ("")
running = True
bound = False
sa = 0
s = 0

# According to the variables defined above, the area under the curve
# will be calculated here in the correct way using if statements. If
# none of the methods are chosen, it will prompt the user with an
# error message and instructions to correctly initiate the program.

while (running == True):
    if bound == False and method == 'left hand sums' or method == 'right hand sums' or method == 'trapezoidal rule' or method == 'midpoint rule' or method == 'all':
        print colored("You are going to use the"), colored(method, 'green', attrs=['underline']), colored("method! \n")
        equation = raw_input("What is your equation? \n        >> ")  # capture an equation written in terms of f
        f = eval("lambda x: " + equation)  # convert the equation string to an actual lamdba function
        n = float(input("How many sections do you want? \n        >> "))  # takes input for how many sections
        a = float(input("What is your lower bound? \n        >> "))  # takes lower bound
        b = float(input("What is your upper bound? \n        >> "))  # takes upper bound
        print ("")
        dx = float((b - a) / n)  # finds change in x
        aa = 0
        a = aa
        s = 0
        if method == 'all':
            # Right hand sums
            while ((a + dx) <= b):  # checks if in x value range
                sa = sa + (f(a) * dx)  # calculates sum at each step
                a = a + dx  # adds dx to the lower x value

            sb = 0
            a = aa

            # Left hand sums
            while a < b - dx:  # checks if in x value range
                sb = sb + (f(a) * dx)  # solves for sum at each step
                a = a + dx  # adds dx to lower x value

            sc = 0
            a = aa

            # Midpoint rule
            while b > a:  # checks if in x value range
                sc = sc + f(a + .5 * dx) * dx  # states the area under the curve
                a = a + dx

            sd = 0
            a = aa

            # Trapezoidal Rule
            while a < b:  # checks if in x value range
                sd = sd + ((f(a) + f(a + dx)) / 2) * dx  # solves for sum at each step
                a = a + dx  # adds dx to lower x value

            print ("Left Hand Sums Area: "), colored(sb, 'green', attrs=['underline'])
            print ("Right Hand Sums Area: "), colored(sa, 'green', attrs=['underline'])
            print ("Midpoint Rule Area: "), colored(sc, 'green', attrs=['underline'])
            print ("Trapezoidal Rule Area: "), colored(sd, 'green', attrs=['underline'])
            running = False

        # solves for left hand sums

        elif method == 'left hand sums':
            while a <= b:  # checks if in x value range
                a = a + dx  # adds dx to the lower x value
                s = s + f(a) * dx  # calculates sum at each step
                print (s)
            print colored("\nThe area under the curve is "), colored(s, 'green', attrs=[
                'underline'])  # states the area under the curve
            running = False

        # solves for midpoint rule

        elif method == 'midpoint rule':
            while b > a:  # checks if in x value range
                s = s + f(a + .5 * dx) * dx  # states the area under the curve
                a = a + dx
                print (s)
            print colored("\nThe area under the curve is "), colored(s, 'green', attrs=[
                'underline'])  # states the area under the curve
            running = False

        # solves with trapezoidal rule

        elif method == 'trapezoidal rule':
            while a < b:  # checks if in x value range
                s = s + ((f(a) + f(a + dx)) / 2) * dx  # solves for sum at each step
                a = a + dx  # adds dx to lower x value
                print (s)
            print colored("\nThe area under the curve is "), colored(s, 'green', attrs=[
                'underline'])  # states the area under the curve
            running = False

        # solves with right hand sums

        elif method == 'right hand sums':
            while a < b:  # checks if in x value range
                s = s + (f(a) * dx)  # solves for sum at each step
                a = a + dx  # adds dx to lower x value
                print (s)
            print colored("\nThe area under the curve is "), colored(s, 'green', attrs=[
                'underline'])  # states the area under the curve
            running = False

        bound = True

# displays error message when a method is not chosen

    else:
        method = method.title()
        cprint ("'{}' is not one of the options. Try one of the following methods.".format(method), 'red')
        print ("    - Left Hand Sums \n    - Right Hand Sums \n    - Midpoint Rule \n    - Trapezoidal Rule")
        method = raw_input("\n Which method would you like to use? \n       >> ").lower()
        print ("")