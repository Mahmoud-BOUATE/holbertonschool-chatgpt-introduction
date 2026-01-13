#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function: Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer whose factorial is to be computed.

    Returns:
    int: The factorial of the number n. For n = 0, returns 1.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    else:
        # Recursive case: n! = n * (n-1)!
        return n * factorial(n-1)

# Read the number from command line arguments
f = factorial(int(sys.argv[1]))

# Print the result
print(f)
