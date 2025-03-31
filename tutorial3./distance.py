import tkinter as tk
from tkinter import messagebox

def calculate_distance():
    try:
       
        initial_height = float(initial_height_entry.get())
        bounciness_index = float(bounciness_index_entry.get())
        number_of_bounces = int(number_of_bounces_entry.get())
        
      
        if initial_height < 0 or bounciness_index < 0 or number_of_bounces < 0:
            raise ValueError("All inputs must be non-negative.")
        
    
        total_distance = initial_height  
        current_height = initial_height
        
        for _ in range(number_of_bounces):
            current_height *= bounciness_index
            total_distance += 2 * current_height 
     
        result_label.config(text=f"Total distance traveled: {total_distance:.2f} units")
    
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = tk.Tk()
root.title("Bouncy Ball Distance Calculator")


tk.Label(root, text="Initial Height (units):").pack(pady=5)
initial_height_entry = tk.Entry(root)
initial_height_entry.pack(pady=5)

tk.Label(root, text="Bounciness Index (0 < index < 1):").pack(pady=5)
bounciness_index_entry = tk.Entry(root)
bounciness_index_entry.pack(pady=5)

tk.Label(root, text="Number of Bounces:").pack(pady=5)
number_of_bounces_entry = tk.Entry(root)
number_of_bounces_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate Distance", command=calculate_distance)
calculate_button.pack(pady=10)


result_label = tk.Label(root, text="")
result_label.pack(pady=10)


root.mainloop()