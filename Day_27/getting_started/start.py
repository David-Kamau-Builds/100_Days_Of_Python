import tkinter as tk
from tkinter.ttk import Button, Entry, Label

FONT = ("Courier", 20, "normal")

def button_clicked():
    new_text = user_input.get()
    my_label.config(text=new_text)

window = tk.Tk()
window.title("My GUI program")
window.minsize(600, 600)
window.config(padx=15, pady=50)

my_label = Label(text="This is a label", font=FONT)
my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1, padx=5, pady=20)

new_button = Button(text="Do not Click Me", command=exit)
new_button.grid(column=2, row=0)

user_input = Entry(width=30)
user_input.grid(column=1, row=2, columnspan=2, pady=10)

window.mainloop()
