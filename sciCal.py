import tkinter as tk
from functools import partial
from math import sqrt, pi, e, log, log10, sin, asin, radians, cos, acos, tan, atan, degrees, gamma
import re

class SciCalculator(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Scientific Calculator")
        self.geometry("750x260")
        self.resizable(False, False)
        self.create_display()
        self.create_buttons()

    def create_display(self):
        self.display = tk.Entry(self, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
        self.display.pack(expand=True, fill="both")

    def create_buttons(self):
        buttons = [
            ["Rad", "Deg", "+/-", "C", "Del", "(", ")", "+"],
            ["sin", "sin⁻¹", "π", "ln", "7", "8", "9", "-"],
            ["cos", "cos⁻¹", "e", "log", "4", "5", "6", "*"],
            ["tan", "tan⁻¹", "1/x", "√", "1", "2", "3", "/"],
            ["x!", "xⁿ", "ⁿ√x", "0", ".", "="]
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
        elif button_text == "C":
            self.display.delete(0, tk.END)
        elif button_text == "Del":
            self.display.delete(len(self.display.get())-1, tk.END)
        elif button_text == "+/-":
            current_text = self.display.get()
            if current_text.startswith("-"):
                self.display.delete(0)
            else:
                self.display.insert(0, "-")
        else:
            self.display.insert(tk.END, button_text)

    def evaluate_expression(self):
        expression = self.display.get()
        expression = expression.replace("sin⁻¹", "asin").replace("cos⁻¹", "acos").replace("tan⁻¹", "atan")
        expression = expression.replace("sin", "sin(radians").replace("cos", "cos(radians").replace("tan", "tan(radians")
        expression = expression.replace("ⁿ√x", "**(1/").replace("√", "sqrt").replace("π", str(pi)).replace("e", str(e))
        expression = expression.replace("log", "log10").replace("ln", "log").replace("ⁿ", "**").replace("1/x", "1/")
        expression = expression.replace("/", "/").replace("*", "*").replace("-", "-").replace("+", "+")
        
        if "!" in expression:
            expression = re.sub(r'(\d+\.\d+|\d+)!', r'gamma(\1+1)', expression)
        try:
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = SciCalculator(root)
    root.mainloop()
