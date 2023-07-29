# Algebra Linear Solver

## Description
Algebra Linear Solver is a project designed to convert and solve algebraic problems. It tokenizes problem statements and converts them into mathematical equations, then solves them using symbolic computation.

## Installation
To get started with the Algebra Linear Solver, you'll need to install certain dependencies:

```bash
pip install nltk sympy
```

Then, download the necessary NLTK data:

```
import nltk
nltk.download('punkt')
```

## Usage
You can use the `convert_to_equation` and `solve_problem` functions to convert problem statements into equations and solve them. Here's an example:

```
problem = "If 5 apples cost 10 dollars, how much does one apple cost?"
print(solve_problem(problem))
```

## Contributing
If you'd like to contribute to the Algebra Linear Solver, please feel free to submit a pull request!

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Contact
For any questions or concerns, please open an issue or contact the repository owner.
