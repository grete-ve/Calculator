from calculator import Calculator
import re

# this is main function
def main():
    # create instance of Calculator class
    calc = Calculator()
    # ask user for input and remove spaces from the input string
    #input_str = input("Enter the expression: ").replace(" ", "")
    input_str = '0-10-10'
    # split the numbers and operators
    numbers = []
    for t in re.split(r'(\d*\.?\d*)', input_str):
        try:
            numbers.append(float(t))
        except ValueError:
            pass

    all_operators = ['+', '-', '*', '/']
    operators = []
    for s in input_str:
        if (s in all_operators):
            operators.append(s)
    
    # check if '*' or '/' is present in operators
    if '*' in operators or '/' in operators:
        # execute the calculation with operator precedence
        result = calc.calculate_with_precedence(numbers, operators)
    else:
        # execute the calculation without operator precedence
        result = calc.calculate(numbers, operators)
    print("Result:", result)


# call main function
if __name__ == "__main__":
    main()