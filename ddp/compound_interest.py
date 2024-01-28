"""
Compound Interest Calculator Function

Objective:
Write a function named 'compound_interest_calculator' to calculate compound interest.

Function Parameters:
1. P (float): Principal amount.
2. r (float): Annual interest rate in decimal.
3. n (integer): Number of times interest is compounded per year.
4. t (integer): Number of years for investment.

Instructions:
- Use the formula: A = P(1 + r/n)^(nt) to calculate compound interest.
- Return the accumulated amount A after t years.
- Handle edge cases for inputs.

Example Test Cases:
1. compound_interest_calculator(1000, 0.05, 12, 5) should calculate the amount.
2. compound_interest_calculator(500, 0.07, 4, 10) should calculate the amount.
3. compound_interest_calculator(1500, 0.03, 6, 7) should calculate the amount.
"""

def compound_interest_calculator(P, r, n, t):
    # Calculating compound interest
    A = P * (1 + r / n) ** (n * t)
    return A

# Example Test Cases
print(compound_interest_calculator(1000, 0.05, 12, 5))  # Compound interest for 1000 at 5% for 5 years compounded 12 times annually
print(compound_interest_calculator(500, 0.07, 4, 10))   # Compound interest for 500 at 7% for 10 years compounded 4 times annually
print(compound_interest_calculator(1500, 0.03, 6, 7))   # Compound interest for 1500 at 3% for 7 years compounded 6 times annually

