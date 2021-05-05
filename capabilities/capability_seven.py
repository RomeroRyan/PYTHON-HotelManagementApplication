import datetime
import tkinter as tk
from capabilities.capability_five import CapabilityFive
from guest_manager import search_guests
from tkinter import *


class CapabilitySeven:
    def __init__(self, frame):
        self.frame = frame
        self.search_flag = "Exact"
        search_title = tk.Label(
            self.frame, text="Guest Search", font=("Times", 20, "bold"))
        search_title.grid(row=0, column=0)
        desc = tk.Label(self.frame, text="Search for guests using any of the following fields:\nGuest First Name, Guest Last Name, Room Number, Phone Number, Street Address, Check In Date, Checkout Date.\n\nDates must be formatted as MM/DD/YYY and Phone numbers must be formatted as ###-###-####.",
                        wraplength=500, justify=LEFT, anchor="w")
        desc.grid(row=1, column=0, columnspan=2, sticky=W, padx=15)

        # search entry field and button
        self.search_entry = tk.Entry(self.frame, width=75)
        self.search_entry.grid(row=2, column=0, padx=15, pady=15)
        search_button = tk.Button(self.frame,
                                  text='Search', command=self.search).grid(row=2, column=1, padx=15, pady=15)

        # toggle buttons for exact match and contains
        self.toggle_val = IntVar()
        exact_btn = Radiobutton(self.frame, text='Exact Match',
                                variable=self.toggle_val, value=0, command=self.set_toggle, borderwidth=0)
        exact_btn.grid(row=3, column=0, sticky=W, padx=15)

        contains_btn = Radiobutton(
            self.frame, text='Contains', variable=self.toggle_val, value=1, command=self.set_toggle, borderwidth=0)
        contains_btn.grid(row=4, column=0, sticky=W, padx=15)

        l = tk.Label(self.frame, text='Search Results:')
        l.grid(sticky=W, row=7, column=0, padx=15)

    def set_toggle(self):
        if self.toggle_val.get() == 0:
            self.toggle_val.set(0)
            self.search_flag = "Exact"
        elif self.toggle_val.get() == 1:
            self.toggle_val.set(1)
            self.search_flag = "Contains"

    def display_results(self, guest_list):

        for offset, guest in enumerate(guest_list):
            msg = "Name: " + guest.get_fname() + " " + guest.get_lname() + " Check in: " + \
                guest.get_chk_in() + " Check out: " + guest.get_chk_out()
            guest_btn = tk.Button(self.frame, text=msg, command=lambda t=guest.get_id(): CapabilityFive(tk.Toplevel(self.frame), t),
                                  width=75, pady=10).grid(row=8+offset, column=0)

    def popup_msg(self, msg):
        popup = tk.Tk()
        popup.wm_title("Error: Unable to save changes")
        label = tk.Label(popup, text=msg)
        label.pack(side="top", fill="x", padx=20, pady=10)
        B1 = tk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()

    def clear_frame(self):
        # destroy all widgets from frame
        for widget in self.frame.winfo_children():
            widget.destroy()
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        self.frame.pack_forget()

    def search(self):
        key = str(self.search_entry.get())
        guests_found = search_guests(self.search_flag, key)
        if len(guests_found) > 0:
            self.clear_frame()
            CapabilitySeven(self.frame)
            self.display_results(guests_found)
        else:
            self.clear_frame()
            CapabilitySeven(self.frame)
            message_label = tk.Label(
                self.frame, text="No results found").grid(row=8, column=0, padx=15, pady=5)
