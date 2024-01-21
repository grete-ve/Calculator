# This is class for creating GUI for calculator

# Importing necessary modules
from models.calculator import Calculator
from models.expression import Expression

# Importing tkinter module
import tkinter as tk
from tkinter import *
    

# this is main function
class CalculatorGUI:
    def __init__(self, root):
        str = ""
        self.expression = Expression(str)
        self.calculator = Calculator()
        self.entry_text = tk.StringVar()
        self.equal_pressed = False

        self.entry_text.trace_add("write", self.input_modified)

        # Set the title of the window
        root.title("Calculator")
        # Set the configuration of the window
        root.geometry("400x200")
        # Set the background color of the window
        root.configure(background="light blue")

        root.bind('<Return>', self.enter_pressed)

        # Create the text entry box
        self.entry = tk.Entry(root, textvariable=self.entry_text, font=('Arial', 14, 'bold'))
        self.entry.grid(row=0, column=0, columnspan=4, ipadx=80, pady=5, ipady=10, padx=10)

        # Create the buttons
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        for i, button_row in enumerate(buttons):
            for j, button_text in enumerate(button_row):
                if button_text == '=':
                    b = tk.Button(root, text=button_text, bg='white', command=self.equalpress, height=1,width=7)
                else:
                    b = tk.Button(root, text=button_text, bg='white', command=lambda text=button_text: self.press(text), height=1,width=7)
                b.grid(row=i+1, column=j)

        # Create clear button
        clear_button = tk.Button(root, text='Clear', bg='white', command=self.clear, height=2,width=8)
        clear_button.grid(row=5, column=0, columnspan=3, pady = 10)

        # Create delete button
        delete_button = tk.Button(root, text='Delete', bg='white', command=self.delete, height=2,width=8)
        delete_button.grid(row=5, column=1, columnspan=3, pady = 10)

    # Function to update the expression as parameter using instance of Expression class when a button is pressed
    def press(self, text):
        if self.equal_pressed and text.isnumeric():
            self.entry_text.set(text)
            self.expression.set(text)
        else:
            self.expression.update(text)
            self.entry_text.set(self.expression.originalExpression)

        self.equal_pressed = False

    def input_modified(self, var, index, mode):

        if self.equal_pressed and self.entry_text.get()[-1].isnumeric():
            self.entry_text.set(self.entry_text.get()[-1])
            self.expression.set(self.entry_text.get())
        else:
            self.expression.set(self.entry_text.get())
        self.equal_pressed = False

    def enter_pressed(self, event):
        self.equalpress()


    # Function to evaluate the final expression when the equal button is pressed
    # calculate the result using instance of Calculator class named calc
    def equalpress(self):
        try:
            result = self.calculator.calculate_with_precedence(self.expression.numbers, self.expression.operators)
            self.entry_text.set(str(result))
            self.expression.set(str(result))
            self.equal_pressed = True
        except Exception as e:
            self.entry_text.set("Error")

    # Function to clear the expression, update the expression state using instance of Expression class and clear the result label
    def clear(self):
        self.expression.clear()
        self.entry_text.set('')

    def delete(self):
        self.expression.delete()
        self.entry_text.set(self.expression.originalExpression)
        self.equal_pressed = False

    def start():
        root = tk.Tk()
        # start the GUI
        gui = CalculatorGUI(root)
        root.mainloop()