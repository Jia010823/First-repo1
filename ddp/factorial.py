"""
Factorial Calculator Function

Objective:
Write a function named 'calculate_factorial' to compute the factorial of a number using a for loop.

Function Parameter:
1. number (integer): A non-negative integer for which the factorial is to be calculated.

Instructions:
- Use a for loop to calculate the factorial of 'number'.
- Return the factorial result.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. calculate_factorial(5) should return the factorial of 5.
2. calculate_factorial(0) should return 1.
3. calculate_factorial(3) should return the factorial of 3.
4. calculate_factorial(-1) should handle negative input.
"""

def calculate_factorial(number):
    # Handling negative input
    if number < 0:
        return "Negative input is not valid"

    # Factorial of 0 is 1
    if number == 0:
        return 1

    # Calculating factorial using a for loop
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i

    return factorial

# Example Test Cases
print(calculate_factorial(5))  # Factorial of 5
print(calculate_factorial(0))  # Factorial of 0
print(calculate_factorial(3))  # Factorial of 3
print(calculate_factorial(-1)) # Negative input handling


