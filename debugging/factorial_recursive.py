#!/usr/bin/python3
import sys

# Calculates factorial using recursion.
# n: Non-negative integer to calculate the factorial of.
# Returns: Factorial of n (int).
def factorial(n):
    if n == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return n * factorial(n - 1)  # Recursive step



# Read input, calculate factorial, and print the result.
f = factorial(int(sys.argv[1]))
print(f)
