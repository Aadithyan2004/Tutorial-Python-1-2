import tkinter as tk
import math

def compute_square_root():

    input_number = float(entry.get())
 
    square_root = math.sqrt(input_number)

    result_label.config(text=f"Square root: {square_root:.2f}")


root = tk.Tk()
root.title("Square Root Calculator")


tk.Label(root, text="Enter a number:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)


tk.Button(root, text="Compute Square Root", command=compute_square_root).pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()