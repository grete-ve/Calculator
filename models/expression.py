from collections import namedtuple
import re

class Expression():
    def __init__(self, expression):
        self.originalExpression = expression
        self.numbers = []
        self.operators = []
        self.split_expression()


    def split_expression(self):
        # split the numbers and operators
        numbers = []
        for t in re.split(r'(\d*\.?\d*)', self.originalExpression):
            try:
                numbers.append(float(t))
            except ValueError:
                pass

        all_operators = ['+', '-', '*', '/']
        operators = []
        for s in self.originalExpression:
            if s in all_operators:
                operators.append(s)
        self.numbers = numbers
        self.operators = operators