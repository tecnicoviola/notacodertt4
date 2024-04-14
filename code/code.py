import tkinter as tk
from tkinter import messagebox

def calculate_factorial():
    try:
        num = int(entry.get())
        if num < 0:
            messagebox.showerror("Error", "Please provide a non-negative integer.")
        else:
            result = factorial(num)
            messagebox.showinfo("Result", f"The factorial of {num} is {result}.")
    except ValueError:
        messagebox.showerror("Error", "Please provide a valid integer.")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Create the main application window
root = tk.Tk()
root.title("Factorial Calculator")

# Create and place widgets
label = tk.Label(root, text="Enter a number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_factorial)
calculate_button.pack()

# Start the application
root.mainloop()
