
class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def substract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Can't divide by zero!")
        return a / b
    
    def calculate(self, numbers, operators):
        result = numbers[0]
        for i in range(len(operators)):
            if operators[i] == "+":
                result = self.add(result, numbers[i+1])
            elif operators[i] == "-":
                result = self.substract(result, numbers[i+1])
            elif operators[i] == "*":
                result = self.multiply(result, numbers[i+1])
            elif operators[i] == "/":
                result = self.divide(result, numbers[i+1])
            else:
                raise ValueError("Invalid operator!")
        return result
    
    def calculate_with_precedence(self, numbers, operators):
        # check if '*' or '/' is present in operators
        if '*' in operators or '/' in operators:
            # execute the calculation with operator precedence
            # find the index of '*' or '/'
            for i in range(len(operators)):
                if operators[i] == '*' or operators[i] == '/':
                    # calculate the result
                    result = self.calculate([numbers[i], numbers[i+1]], [operators[i]])
                    # replace the first number with result
                    numbers[i] = result
                    # remove the second number and operator
                    numbers.pop(i+1)
                    operators.pop(i)
                    # recursively call the same method
                    return self.calculate_with_precedence(numbers, operators)
        else:
            # execute the calculation without operator precedence
            result = self.calculate(numbers, operators)

        if result.is_integer():
            result = int(result)
            
        return result