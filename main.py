from tkinter import *

window = Tk()
window.title("This is a miles to kilometers calculator.")
window.config(padx=10, pady=10)

# def change_label():
#     label.config(text=entry.get())
#
#
# label = Label(text="This is the label", font=("Arial", 20, "normal"))
# label.grid(column=0, row=0)
#
#
# button = Button(text="Please click me!", font=("Arial", 10, "normal"), command=change_label)
# button.grid(column=1, row=1)
#
#
# new_button = Button(text="Please click me!", font=("Arial", 10, "normal"), command=change_label)
# new_button.grid(column=2, row=0)
#
#
# entry = Entry()
# entry.grid(column=3, row=2)


def convert_miles_to_km():
    kilos = round(float(miles_input.get()) * 1.609, 2)
    in_km.config(text=kilos)


# Column 1
equal_to = Label(text="is equal to:", font=("Arial", 15, "normal"))
equal_to.grid(column=0, row=1)

# Column 2

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

in_km = Label(text=0, font=("Arial", 11, "normal"))
in_km.grid(column=1, row=1)

calculate_button = Button(text="Calculate!", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)

# Column 3

miles = Label(text="Miles", font=("Arial", 15, "normal"))
miles.grid(column=2, row=0)

km = Label(text="Km", font=("Arial", 15, "normal"))
km.grid(column=2, row=1)

mainloop()
