import tkinter as tk
from tkinter import messagebox
import math

def compute_square_root():
    try:
      
        input_number = int(entry.get())
        
       
        if input_number < 0:
            raise ValueError("Please enter a non-negative integer.")
        
     
        square_root = math.sqrt(input_number)
        
     
        result_label.config(text=f"Square root: {square_root:.2f}")
    except ValueError as e:
       
        messagebox.showerror("Input Error", str(e))


root = tk.Tk()
root.title("Square Root Calculator")


tk.Label(root, text="Enter a non-negative integer:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)


tk.Button(root, text="Compute Square Root", command=compute_square_root).pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()