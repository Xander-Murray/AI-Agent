import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output

MANUAL = '''
Calculator Manual

Usage: python main.py "<expression1>" "<expression2>" ...

This script evaluates mathematical expressions using the Calculator class.

Supported operations:
  - Addition: +
  - Subtraction: -
  - Multiplication: *
  - Division: /
  - Exponentiation: ^
  - Square Root: sqrt(x)
  - Modulo: %
  - Logarithm (base e): log(x)

Constants:
  - pi: Represents the value of pi (approximately 3.14159)

Examples:
  - python main.py "3 + 5" "10 / 2"
  - python main.py "2 ^ 3" "sqrt 16"
  - python main.py "log 2.71828"
  - python main.py "10 % 3"
  - python main.py "pi * 2"

Operator Precedence:
  1. Parentheses ()
  2. Square Root (sqrt), Logarithm (log)
  3. Exponentiation (^)
  4. Multiplication (*), Division (/), Modulo (%)
  5. Addition (+), Subtraction (-)

Error Handling:
  - The calculator handles division by zero, square roots of negative numbers,
    invalid tokens, unmatched parentheses, and incorrect number of operands.

Note: Expressions should be space-separated.
'''


def main():
    calculator = Calculator()

    if len(sys.argv) <= 1:
        print(MANUAL)
        return

    expressions = sys.argv[1:]
    for expression in expressions:
        try:
            result = calculator.evaluate(expression)
            if result is not None:
                to_print = format_json_output(expression, result)
                print(to_print)
            else:
                print(f"Error: Expression '{expression}' is empty or contains only whitespace.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
