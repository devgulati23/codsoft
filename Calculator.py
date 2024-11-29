import tkinter as tk
def on_click(button_text):
    """Handles button clicks."""
    if button_text == "=":
        calculate()
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

def calculate():
    """Evaluates the expression in the entry field."""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def on_key(event):
    """Handles keyboard input."""
    key = event.char
    if key in "0123456789+-*/.=":
        if key == "=":
            calculate()
        else:
            entry.insert(tk.END, key)
    elif key == "\r":  # Enter key
        calculate()
    elif key == "\x08":  # Backspace key
        entry.delete(len(entry.get())-1, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create an entry widget for input/output
entry = tk.Entry(root, width=20, font=("Arial", 18), bd=5, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Bind keyboard events
root.bind("<Key>", on_key)

# Button texts
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Create buttons and place them in the window
row_val, col_val a x=button: on_click(x)
    tk.Button(root= 1, 0
for button in buttons:
    action = lambd, text=button, width=5, height=2, font=("Arial", 14), command=action).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the event loop
root.mainloop()
