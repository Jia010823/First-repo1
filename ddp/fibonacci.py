"""
Fibonacci Sequence Calculator Function

Objective:
Write a function named 'fibonacci_sequence' to generate the Fibonacci sequence up to a given number using a while loop.

Function Parameter:
1. max_value (integer): Maximum value for the Fibonacci sequence.

Instructions:
- Use a while loop to generate the Fibonacci sequence up to 'max_value'.
- Return the sequence as a list.
- Handle edge cases for 0 and negative inputs.

Example Test Cases:
1. fibonacci_sequence(10) should return the Fibonacci sequence up to 10.
2. fibonacci_sequence(1) should return the Fibonacci sequence up to 1.
3. fibonacci_sequence(0) should return a sequence with 0.
4. fibonacci_sequence(-5) should handle negative input.
"""

def fibonacci_sequence(max_value):
    if max_value < 0:  # Handling negative input
        return "Negative input is not valid"
    if max_value == 0:  # Handling 0 input
        return [0]

    # Initializing the first two numbers
    fib_sequence = [0, 1]

    # Generating the Fibonacci sequence
    while True:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        if next_number > max_value:
            break
        fib_sequence.append(next_number)

    return fib_sequence

# Example Test Cases
print(fibonacci_sequence(10))  # Should return the Fibonacci sequence up to 10
print(fibonacci_sequence(1))   # Should return the Fibonacci sequence up to 1
print(fibonacci_sequence(0))   # Should return [0]
print(fibonacci_sequence(-5))  # Should handle negative input

