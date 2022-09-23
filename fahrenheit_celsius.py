import tkinter as tk
from tkinter import W
from tkinter import ttk

window = tk.Tk()

lbl_fahrenheit = tk.Label(
    master = window,
    text = 'Fahrenheit: '
)

ent_fahrenheit = ttk.Entry(
    master = window,
)

lbl_celsius_result = tk.Label(
    master = window,
    font = ('Arial Bold', 9)
)

def fahrenheit_celsius_convert():
    try:
        lbl_celsius_result['text'] = float(ent_fahrenheit.get())
        lbl_celsius_result['text'] = round((lbl_celsius_result['text'] - 32) * (5/9) , 2)
    except ValueError:
        if ent_fahrenheit.get() != '':
            lbl_celsius_result['text'] = 'Enter a number!'
        else:
            lbl_celsius_result['text'] ='Input is empty!'

btn_calc = ttk.Button(
    master = window,
    text = 'Calc!',
    command = fahrenheit_celsius_convert,
)

lbl_celsius = tk.Label(
    master = window,
    text = 'Celsius: '
)

lbl_fahrenheit.grid(row = 0, column = 0, pady = 10, padx = 10)
ent_fahrenheit.grid(row = 0, column = 1, pady = 10)
btn_calc.grid(row = 0, column = 2, padx = 20)
lbl_celsius.grid(row = 1, column = 0, padx = 10, pady = (2,20), sticky = (W, ))
lbl_celsius_result.grid(row = 1, column = 1, padx = 10, pady = (2,20))

window.mainloop()