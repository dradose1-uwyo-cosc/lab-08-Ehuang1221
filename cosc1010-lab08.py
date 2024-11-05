# Edmon Huang
# UWYO COSC 1010
# Submission Date: 11/05/2024
# Lab 08
# Lab Section: 11
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def convert_to_number(value):
    if '.' in value:
        try: 
            float_value = float(value) # converts to float
            if value.count('.') == 1: # makes sure there's only one decimal
                return float(value) # Returns float
            else:
                return False # If more than one decimal, returns false
        except ValueError:
            return False # If conversion fails, returns false
    else:
        try:
            return int(value)
        except ValueError:
            return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false


# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_x, upper_x):
    if not (isinstance(lower_x, int) and isinstance(upper_x, int)) or lower_x > upper_x: # checks if lower_x and upper_x are integers
        return False # returns false if not true
    if lower_x >= upper_x:
        return False # False if lower is greater than upper
    y_values = [] # empty list
    for x in range(lower_x, upper_x + 1): #goes through each x in range
        y = m * x + b
        y_values.append(y) # adds y to list
    return y_values # returns list of y

while True: # Loops through while user enters values
    m = input("Enter slope m or 'exit' to quit: ")
    if m == 'exit': # breaks if exit
        break
    b = input("Enter y-intercept b or 'exit' to quit: ")
    lower_x = input("Enter lower x bound or 'exit' to quit: ")
    upper_x = input("Enter upper x bound or 'exit' to quit: ")

    # convert inputs
    m = convert_to_number(m)
    b = convert_to_number(b)
    lower_x = convert_to_number(lower_x)
    upper_x = convert_to_number(upper_x)

    # Checks if input is valid
    if m is False or b is False or not isinstance(lower_x, int) or not isinstance(upper_x, int):
        print("Invalid")
    else:
        y_values = slope_intercept(m, b, lower_x, upper_x)
        if y_values is False:
            print("Invalid")
        else:
            print("y values are: ", y_values)
print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
import math
def square_root(value): # square root function
    if value < 0:
        return None # if negative return null
    return math.sqrt(value) # finds square root

def Quadratic_formula(a, b, c): # quadratic eqaution function
    discriminant = b ** 2 - (4 * a * c) # discriminant 
    sqrt_discriminant = square_root(discriminant) # square roots the discriminant
    if sqrt_discriminant is None:
        return None # no solution
    x1 = (-b + sqrt_discriminant) / (2 * a) # root 1
    x2 = (-b - sqrt_discriminant) / (2 * a) # root 2
    return x1, x2 # 2 solutions

while True:
    a = input("Enter a or 'exit' to quit: ")
    if a == 'exit':
        break
    b = input("Enter b: ")
    c = input("Enter c: ")

    # converts numbers
    a = convert_to_number(a)
    b = convert_to_number(b)
    c = convert_to_number(c)

    if a is False or b is False or c is False:
        print("Invalid") # invalid inputs
    else: # calls the quadratic formula function
        roots = Quadratic_formula(a, b, c)
        if roots is None:
            print("No real solution") # if no real roots
        else:
            print("Solutions:", roots)



