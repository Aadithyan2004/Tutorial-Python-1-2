import tkinter as tk

def convert_to_uppercase():
    result_label.config(text=input_entry.get().upper())


root = tk.Tk()
root.title("Uppercase Converter")

input_entry = tk.Entry(root, width=50)
input_entry.pack(pady=10)


convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=5)


result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)


root.mainloop()