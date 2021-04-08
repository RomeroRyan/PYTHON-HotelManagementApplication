import tkinter as tk
from tkinter import *


class CapabilitySeven(Frame):
    def __init__(self, frame):
        search_title = tk.Label(
            frame, text="Guest Search", font=("Times", 20, "bold"))
        search_title.grid(row=0, column=0)
        desc = tk.Label(frame, text="Search for guests using any of the following fields: Guest First Name, Guest Last Name, Room Number, Phone Number, Street Address, Check In Date, Checkout Date. Dates must be formatted as MM/DD/YYY and Phone numbers must be formatted as ###-###-####.",
                        wraplength=500, justify=LEFT, anchor="w")
        desc.grid(row=1, column=0, columnspan=2, sticky=W, padx=15)

        # search entry field and button
        e1 = tk.Entry(frame, width=75)
        e1.grid(row=2, column=0, padx=15, pady=15)
        search_button = tk.Button(frame,
                                  text='Search').grid(row=2, column=1, padx=15, pady=15)
        search_flag = BooleanVar(value=True)

        # toggle buttons for exact match and contains
        c1 = Radiobutton(frame, text='Exact Match', variable=search_flag,
                         value=1, borderwidth=0)
        c1.grid(row=3, column=0, sticky=W, padx=15)
        c2 = Radiobutton(frame, text='Contains', variable=search_flag,
                         value=0, borderwidth=0)
        c2.grid(row=4, column=0, sticky=W, padx=15)

        l = tk.Label(frame, text='Search Results:')
        l.grid(sticky=W, row=7, column=0, padx=15, pady=15)
        sep = tk.Label(
            frame, text='---------------------------------------------------------')
        sep.grid(sticky=W, row=8, column=0, padx=15)
        # Placeholder for now
        sample_result = tk.Label(
            frame, text='John Doe - Room 101 Check In: 03/29/2021, Checkout: 04/04/2021')
        sample_result.grid(sticky=W, row=9, column=0, padx=15)
        sample_result = tk.Label(
            frame, text='Phone #: 123-456-7890 Address: 123 Sesame Street New York, NY')
        sample_result.grid(sticky=W, row=10, column=0, padx=15)
        sep = tk.Label(
            frame, text='---------------------------------------------------------')
        sep.grid(sticky=W, row=11, column=0, padx=15)
