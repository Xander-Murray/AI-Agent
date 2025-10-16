import math

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b if b != 0 else self._raise_value_error("Division by zero"),
            "^": lambda a, b: a ** b,  # Exponentiation
            "sqrt": lambda a: math.sqrt(a) if a >= 0 else self._raise_value_error("Square root of negative number"), # Square root
            "%": lambda a, b: a % b if b != 0 else self._raise_value_error("Division by zero (modulo)"),
            "log": lambda a: math.log(abs(a)),
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
            "^": 3, # higher precedence for exponentiation
            "sqrt": 3,
            "%": 2,
            "log": 3,
        }

        self.constants = {
            "pi": math.pi
        }

    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token == '(': 
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':  
                    self._apply_operator(operators, values)
                if operators:
                    operators.pop()  # Remove the '('
                else:
                    self._raise_value_error("Unmatched ')'")
            elif token in self.operators:
                while (
                    operators
                    and operators[-1] != '('  
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                try:
                    if token in self.constants:
                        values.append(self.constants[token])
                    else:
                        num = float(token)
                        values.append(num)
                except ValueError:
                    self._raise_value_error(f"invalid token: {token}")

        while operators:
            if operators[-1] == '(':  
                self._raise_value_error("Unmatched '('")
            self._apply_operator(operators, values)

        if len(values) != 1:
            self._raise_value_error("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if operator == "sqrt" or operator == "log":
            if not values:
                self._raise_value_error(f"not enough operands for operator {operator}")
            a = values.pop()
            values.append(self.operators[operator](a))
        else:
            if len(values) < 2:
                self._raise_value_error(f"not enough operands for operator {operator}")
            b = values.pop()
            a = values.pop()
            values.append(self.operators[operator](a, b))

    def _raise_value_error(self, message):
        raise ValueError(message)
