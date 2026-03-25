import tkinter as tk
import math

# Window setup
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("320x500")
root.configure(bg="#1e1e1e")

# Entry field
entry = tk.Entry(root, width=20, font=("Arial", 20), bd=5, bg="#2c2c2c", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

history = []

# ---------------- FUNCTIONS ---------------- #

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current[:-1])

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        history.append(f"{expression} = {result}")
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def show_history():
    window = tk.Toplevel(root)
    window.title("History")
    window.configure(bg="#1e1e1e")

    for item in history:
        tk.Label(window, text=item, fg="white", bg="#1e1e1e").pack()

def scientific(func):
    try:
        value = float(entry.get())
        if func == "sin":
            result = math.sin(value)
        elif func == "cos":
            result = math.cos(value)
        elif func == "tan":
            result = math.tan(value)
        elif func == "sqrt":
            result = math.sqrt(value)
        elif func == "log":
            result = math.log10(value)

        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Keyboard support
def key_event(event):
    key = event.char
    if key in "0123456789+-*/.":
        click(key)
    elif key == "\r":
        calculate()
    elif key == "\x08":
        backspace()

root.bind("<Key>", key_event)

# ---------------- STYLES ---------------- #

base_style = {"font": ("Arial", 12), "width": 5, "height": 2}

number_style = {**base_style, "bg": "#2c3e50", "fg": "white"}
operator_style = {**base_style, "bg": "#e67e22", "fg": "white"}
equal_style = {**base_style, "bg": "#27ae60", "fg": "white"}
clear_style = {**base_style, "bg": "#e74c3c", "fg": "white"}

# ---------------- BUTTONS ---------------- #

buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('+',4,2)
]

for (text, row, col) in buttons:
    style = operator_style if text in "+-*/" else number_style

    tk.Button(
        root,
        text=text,
        command=lambda t=text: click(t),
        **style
    ).grid(row=row, column=col, padx=3, pady=3)

# Special buttons
tk.Button(root, text="=", command=calculate, **equal_style).grid(row=4, column=3, padx=3, pady=3)
tk.Button(root, text="C", command=clear, **clear_style).grid(row=5, column=0, padx=3, pady=3)
tk.Button(root, text="⌫", command=backspace, **number_style).grid(row=5, column=1, padx=3, pady=3)
tk.Button(root, text="History", command=show_history, **number_style).grid(row=5, column=2, columnspan=2, padx=3, pady=3)

# Scientific buttons
tk.Button(root, text="sin", command=lambda: scientific("sin"), **number_style).grid(row=6, column=0, padx=3, pady=3)
tk.Button(root, text="cos", command=lambda: scientific("cos"), **number_style).grid(row=6, column=1, padx=3, pady=3)
tk.Button(root, text="tan", command=lambda: scientific("tan"), **number_style).grid(row=6, column=2, padx=3, pady=3)
tk.Button(root, text="√", command=lambda: scientific("sqrt"), **number_style).grid(row=6, column=3, padx=3, pady=3)
tk.Button(root, text="log", command=lambda: scientific("log"), **number_style).grid(row=7, column=0, padx=3, pady=3)

# Run app
root.mainloop()