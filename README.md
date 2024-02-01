# About The Project

The Calculator project is a Python-based application that provides a Graphical User Interface (GUI) for performing basic mathematical operations. The project is structured as follows:

```bash
Calculator
├── models
│   ├── __init__.py
│   ├── calculator.py
│   ├── calculatorGUI.py
│   └── expression.py
├── tests
│   ├── __init__.py
│   └── test_calculator.py
├── __init__.py
└── main.py
```

### Core Components

- Calculator Logic: The calculator.py module contains the Calculator class. This class provides methods for basic mathematical operations such as addition, subtraction, multiplication, and division.

- Graphical User Interface: The calculatorGUI.py module contains the CalculatorGUI class. This class provides a graphical user interface for the calculator, using the Calculator class to perform the calculations.

- Expression Parsing: The expression.py module contains the Expression class. This class is used to take the user's input as a string, parse it into a mathematical expression, and evaluate the result.

### Usage

The file main.py is the entry point of the application. It creates an instance of the CalculatorGUI class and starts the GUI event loop.

To run the calculator application, navigate to the project directory and run the following command to start the GUI:

```
python main.py
```

### Testing

To run the tests, navigate to the project directory and run the following command:

```
python -m unittest discover tests
```
