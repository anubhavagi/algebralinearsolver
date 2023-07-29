import nltk
from nltk import pos_tag, word_tokenize
from sympy import symbols, Eq, solve
import re

def is_number(s):
    """Check whether a string represents a number."""
    return re.fullmatch(r'[0-9]+', s) is not None

# First, we define a function to convert the problem to an equation
def convert_to_equation(problem):
    text = word_tokenize(problem) # Tokenizing the problem
    pos = pos_tag(text) # Part-of-speech tagging

    # We're looking for number-noun pairs (like "5 apples") to convert into variables
    variables = [word for word, tag in pos if tag in ('CD', 'NNS', 'NN')]

    # Convert the variable to a sympy symbol and the number to an integer
    # This assumes that each number is immediately followed by its corresponding variable
    # This is a simplification and may not always be true!
    equation_parts = [int(variables[i]) if is_number(variables[i]) else symbols(variables[i]) for i in range(len(variables))]

    # Create a sympy equation from the parts
    # This assumes that the problem can be represented as a simple equation of the form aX = b
    # This is a simplification and may not always be true!
    equation = Eq(equation_parts[0]*equation_parts[1], equation_parts[2])

    return equation

# Now, we can define a function to solve the problem
def solve_problem(problem):
    equation = convert_to_equation(problem)
    solution = solve(equation)
    return solution

# Example usage:
problem = "If 5 apples cost 10 dollars, how much does one apple cost?"
print(solve_problem(problem))
