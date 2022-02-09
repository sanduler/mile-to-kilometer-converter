# Name: Ruben Sanduleac
# Description: A simple GUI using tkinter for converting mile to kilometer
import tkinter

FACTOR = 1.609

# create a window object from the Tk class
window = tkinter.Tk()
# change the title of the GUI
window.title("Mile/Km Converter")
# set the size of the window
window.minsize(width=280, height=70)
window.config(padx=10, pady=10)
equal_to = tkinter.Label()
equal_to.config(text="is equal to")
equal_to.grid(column=0, row=1)

miles_entry = tkinter.Entry()
miles_entry.config(width=10)
miles_entry.grid(column=1, row=0)

miles_label = tkinter.Label()
miles_label.config(text="Mile(s)")
miles_label.grid(column=2, row=0)

km_entry = tkinter.Entry()
km_entry.config(width=10)
km_entry.grid(column=1, row=1)

km_label = tkinter.Label()
km_label.config(text="Kilometer(s)")
km_label.grid(column=2, row=1)

def convert_to_kilo():
    number = float(miles_entry.get())
    total = str(number * FACTOR)
    km_entry.insert(1, string=total)

def convert_to_miles():
    number = float(km_entry.get())
    total = str(number / FACTOR)
    miles_entry.insert(1, string=total)

def clear():
    # miles_entry.insert(0, tkinter.END)
    km_entry.delete(0, tkinter.END)
    miles_entry.delete(0, tkinter.END)


button = tkinter.Button(text="Calculate Km", command=convert_to_kilo)
button.grid(column=1, row=2)

button = tkinter.Button(text="Calculate Miles", command=convert_to_miles)
button.grid(column=2, row=2)

button = tkinter.Button(text="Clear", command=clear)
button.grid(column=0, row=2)

window.mainloop()