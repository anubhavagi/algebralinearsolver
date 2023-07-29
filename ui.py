# Import necessary libraries
import download
import streamlit as st
import sys
sys.path.insert(0, '/path_to_your_script/')  # replace with the path to your maths.py script
from maths import convert_to_equation, solve_problem

# Create the Streamlit application
def main():
    st.title("Word Problem Solver")

    st.markdown("Please input questions that are in the form of linear equations (ax + b = c). For example:")
    st.markdown("- 'If 5 apples cost 10 dollars, how much does one apple cost?'")
    st.markdown("- 'A car and a bike together cost $5000. The car costs $4000 more than the bike. What is the cost of the bike?'")

    # Create a text input for the word problem
    problem = st.text_input('Enter your word problem')

    if st.button('Solve'):
        if problem:
            try:
                # Convert the problem to an equation
                equation = convert_to_equation(problem)
                
                # Solve the problem
                solution = solve_problem(problem)

                # Display the equation and solution
                st.write("Equation: ", str(equation))
                st.write("Solution: ", solution)
            except Exception as e:
                st.write("An error occurred: ", str(e))
        else:
            st.write("Please enter a word problem")

if __name__ == "__main__":
    main()
