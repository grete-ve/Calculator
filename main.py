from models.calculator import Calculator
from models.expression import Expression

# this is main function
def main():
    global SplitExpression
    # create instance of Calculator class
    calc = Calculator()
    # ask user for input and remove spaces from the input string
    #input_str = input("Enter the expression: ").replace(" ", "")
    input_str = '10 * 2 / 2 + 1 * 4'
    expression = Expression(input_str)

    result = calc.calculate_with_precedence(expression.numbers, expression.operators)
    print("Result:", result)


# call main function
if __name__ == "__main__":
    main()