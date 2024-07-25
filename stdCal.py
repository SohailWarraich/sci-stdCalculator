import tkinter as tk
from functools import partial
from math import sqrt
import re

class StdCalculator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Standard Calculator")
        self.geometry("430x320")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.display = tk.Label(self, text="", anchor="e", font=("Arial", 20), bg="white", relief="groove")
        self.display.pack(expand=True, fill="both")

        buttons = [
            ["Clear", "Del", "(", ")", "÷"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "√", "xⁿ", "="]
        ]

        for row_values in buttons:
            row = tk.Frame(self)
            row.pack(expand=True, fill="both")
            for button_text in row_values:
                button = tk.Button(row, text=button_text, font=("Arial", 18), command=partial(self.on_button_click, button_text))
                button.pack(side="left", expand=True, fill="both")

    def on_button_click(self, button_text):
        if button_text == "=":
            self.evaluate_expression()
        elif button_text == "Clear":
            self.display.config(text="")
        elif button_text == "Del":
            current_text = self.display.cget("text")
            self.display.config(text=current_text[:-1])
        elif button_text == "√":
            current_text = self.display.cget("text")
            self.display.config(text=current_text + "sqrt")
        elif button_text == "xⁿ":
            current_text = self.display.cget("text")
            self.display.config(text=current_text + "**")
        else:
            current_text = self.display.cget("text")
            self.display.config(text=current_text + button_text)

    def evaluate_expression(self):
        expression = self.display.cget("text")
        expression = expression.replace("÷", "/").replace("sqrt", "sqrt")
        try:
            result = eval(expression)
            self.display.config(text=str(result))
        except Exception:
            self.display.config(text="Error")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = StdCalculator(root)
    root.mainloop()
