import tkinter as tk
from stdCal import StdCalculator
from sciCal import SciCalculator

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("200x150")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        std_cal = tk.Button(self, text="Standard Calculator", command=self.open_std_cal)
        std_cal.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        sci_cal = tk.Button(self, text="Scientific Calculator", command=self.open_sci_cal)
        sci_cal.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def open_std_cal(self):
        StdCalculator(self)

    def open_sci_cal(self):
        SciCalculator(self)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()
