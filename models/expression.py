
from collections import namedtuple
import re

class Expression():
    def __init__(self, expression):
        self.originalExpression = expression
        self.numbers = []
        self.operators = []
        self.split_expression()

    # This function is used to split the expression into numbers and operators.
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

    # This function is used to set the expression and split the expression into
    # numbers and operators.
    def set(self, text):
        self.originalExpression = text
        self.split_expression()

    # This function is used to update the expression when a button is pressed
    # in the text entry box. This function is called in main.py file.
    def update(self, text):
        self.originalExpression += text
        self.split_expression()

    # This function is used to clear the expression and the numbers and operators
    # stored in the instance of Expression class. This function is called in main.py file.
    def clear(self):
        self.originalExpression = ""
        self.numbers = []
        self.operators = []

    # This function is used to delete the last character from the expression and
    # update the numbers and operators stored in the instance of Expression class.
    def delete(self):
        self.originalExpression = self.originalExpression[:-1]
        self.split_expression()