#!/usr/bin/python3
"""
Simple GUI Calculator in Python
"""
import tkinter as tk
from tkinter import *


# String that will contain the operation to be calculated:
calculation = ""

# Creates the essential functions:
def add_to_calculation(element):
    """Adds all our elements in the calculation string to execute the operation"""
    global calculation
    calculation += str(element)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    """Executes the operation saved in the calculation string"""
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except:
        clear_field()
        text_result.insert(1.0, "Error!    ┐(´•_•`)┌")

def clear_field():
    """Clears the calculator visor"""
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Creates the interface:
root = tk.Tk()
root.title("Cute calculator uwu")
root.geometry("350x380")

my_icon = PhotoImage(file="images/cat.png")
root.iconphoto(False, my_icon)
# Window with constant size:
root.minsize(350, 380)
root.maxsize(350, 380)

root.configure(bg="#efe1fc")

text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)

# Configurates the buttons and events:
# NUMBERS:
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_1.configure(bg="#d4b6f0")

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_2.configure(bg="#d4b6f0")

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_3.configure(bg="#d4b6f0")

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_4.configure(bg="#d4b6f0")

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_5.configure(bg="#d4b6f0")

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_6.configure(bg="#d4b6f0")

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_7.configure(bg="#d4b6f0")

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_8.configure(bg="#d4b6f0")

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)
btn_9.configure(bg="#d4b6f0")

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)
btn_0.configure(bg="#d4b6f0")
# OPERATORS:
btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_add.grid(row=2, column=4)
btn_add.configure(bg="#c586e3")

btn_sub = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_sub.grid(row=3, column=4)
btn_sub.configure(bg="#c586e3")

btn_mul = tk.Button(root, text="x", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mul.grid(row=4, column=4)
btn_mul.configure(bg="#c586e3")

btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)
btn_div.configure(bg="#c586e3")

btn_open = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_open.grid(row=5, column=1)
btn_open.configure(bg="#c190f0")

btn_close = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_close.grid(row=5, column=3)
btn_close.configure(bg="#c190f0")
# CLEAR AND EQUAL:
btn_clear = tk.Button(root, text="Clear", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)
btn_clear.configure(bg="#f6f0fc")

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equal.grid(row=6, column=3, columnspan=2)
btn_equal.configure(bg="#f6f0fc")

# Image:
my_img = tk.PhotoImage(file="./images/cutecats.gif")
my_img = my_img.subsample(2, 2)
my_label = tk.Label(root, image=my_img)
my_label.grid(row=7, column=1, columnspan=4, sticky='nsew')
my_label.configure(bg="#efe1fc")


# tkinter event loop:
root.mainloop()
