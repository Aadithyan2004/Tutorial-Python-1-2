import tkinter as tk

def convert_to_uppercase():
  
    input_string = entry.get()
   
    uppercase_string = input_string.upper()
   
    result_label.config(text=uppercase_string)


root = tk.Tk()
root.title("String to Uppercase Converter")

input_label = tk.Label(root, text="Enter a string:")
input_label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)


convert_button = tk.Button(root, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack(pady=10)


result_label = tk.Label(root, text="", font=("Helvetica", 14))
result_label.pack(pady=10)


root.mainloop()