from calculator import Calculator

# this is main function
def main():
    # create instance of Calculator class
    calc = Calculator()
    # ask user for input and remove spaces from the input string
    input_str = input("Enter the expression: ").replace(" ", "")
    
    # split the numbers and operators
    numbers = [int(input_str[i]) for i in range(0, len(input_str), 2)]
    operators = [input_str[i] for i in range(1, len(input_str), 2)]
    
    # check if '*' or '/' is present in operators
    if '*' in operators or '/' in operators:
        # execute the calculation with operator precedence
        result = calc.calculate_with_precedence(numbers, operators)
    else:
        # execute the calculation without operator precedence
        result = calc.calculate(numbers, operators)
    print("Result:", result)


# call main function
main()