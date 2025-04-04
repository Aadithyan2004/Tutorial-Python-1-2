import tkinter as tk
from tkinter import messagebox
import math

def calculate_square_root():
    user_input = entry.get()
    try:
        number = float(user_input)  
        if number < 0:
            raise ValueError("Please enter a non-negative number.")
        result = math.sqrt(number)
        result_label.config(text=f"Square root: {result:.2f}")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))


root = tk.Tk()
root.title("Square Root Calculator")


entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate", command=calculate_square_root)
calculate_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()