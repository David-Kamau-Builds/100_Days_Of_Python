import tkinter as tk
from tkinter.ttk import Button, Entry, Label

FONT = ("Courier", 14, "normal")

def calculate_km():
    miles = float(user_input.get())
    km = miles * 1.60934
    km_result_label.config(text=f"{km:.2f}")

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry for miles
user_input = Entry(width=10)
user_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)

km_result_label = Label(text="0", font=FONT)
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=2, row=1)

# Calculate button
button = Button(text="Calculate", command=calculate_km)
button.grid(column=1, row=2, pady=10)

window.mainloop()
