#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function calculates the factorial of a given number 'n' recursively. 
    The factorial of a number 'n' is the product of all positive integers less than or equal to 'n'.
    
    Parameters:
    n (int): The number for which the factorial is to be calculated. The factorial of 0 is defined as 1.

    Returns:
    int: The factorial of the number 'n'. If 'n' is 0, it returns 1. For any positive integer 'n', 
         it returns the product of all integers from 'n' down to 1.
    """
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive case: n * factorial of (n-1)

# Reading the argument passed to the script (the number for which factorial is to be calculated)
f = factorial(int(sys.argv[1]))

# Printing the result
print(f)
