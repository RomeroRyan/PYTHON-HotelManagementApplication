import tkinter as tk
import os
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk, ImageOps


class CapabilityFive:
    def __init__(self, frame):
        self.frame = Tk()
        profile_title = tk.Label(
            frame, text="Guest Profile", font=("Times", 20, "bold"))
        profile_title.grid(row=0, column=0)
        btn = Button(frame, text='replace image').grid(row=2, column=0)

        # create the labels for each field
        fname_label = tk.Label(frame, text="First Name",
                               anchor='w', width=20).grid(row=3, column=0, padx=15, pady=15)
        lname_label = tk.Label(frame, text="Last Name", anchor='w',
                               width=20).grid(row=4, column=0, padx=15, pady=15)
        phone_label = tk.Label(frame, text="Phone Number",
                               anchor='w', width=20).grid(row=5, column=0, padx=15, pady=15)
        address_label = tk.Label(frame, text="Address",
                                 anchor='w', width=20).grid(row=6, column=0, padx=15, pady=15)
        email_label = tk.Label(frame, text="E-mail", anchor='w',
                               width=20).grid(row=7, column=0, padx=15, pady=15)
        id_label = tk.Label(frame, text="ID", anchor='w',
                            width=20).grid(row=8, column=0, padx=15, pady=15)
        vehicle_label = tk.Label(frame, text="Vehicle License Plate",
                                 anchor='w', width=20).grid(row=9, column=0, padx=15, pady=15)

        # create the fields
        fname_field = tk.Entry(frame)
        fname_field.grid(row=3, column=1, padx=15, pady=15)
        lname_field = tk.Entry(frame)
        lname_field.grid(row=4, column=1, padx=15, pady=15)
        phone_field = tk.Entry(frame)
        phone_field.grid(row=5, column=1, padx=15, pady=15)
        address_field = tk.Entry(frame)
        address_field.grid(row=6, column=1, padx=15, pady=15)
        email_field = tk.Entry(frame)
        email_field.grid(row=7, column=1, padx=15, pady=15)
        id_field = tk.Entry(frame)
        id_field.grid(row=8, column=1, padx=15, pady=15)
        vehicle_field = tk.Entry(frame)
        vehicle_field.grid(row=9, column=1, padx=15, pady=15)

        # populate fields with first guest's information (fixed values for now)
        x = "./res/placeholder.png"
        img = Image.open(x)
        img = img.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        panel = Label(frame, image=img)
        panel.image = img
        panel.grid(row=1, column=0, padx=15, pady=15)

        fname_field.insert(0, "John")
        lname_field.insert(0, "Doe")
        phone_field.insert(0, "203-456-7890")
        address_field.insert(0, "203 sesame st")
        email_field.insert(0, "john@gmail.com")
        id_field.insert(0, "Y1234567")
        vehicle_field.insert(0, "POGGERS")

        # display previous profile
        prev_btn = tk.Button(frame, text="Prev", anchor=tk.W,
                             width=10).grid(row=10, column=0, pady=15)
        # save changes to profile
        save_btn = tk.Button(frame, text="Save", anchor=tk.W,
                             width=10).grid(row=10, column=1, pady=15)
        # display next profile
        nxt_btn = tk.Button(frame, text="Next", anchor=tk.W,
                            width=10).grid(row=10, column=2, pady=15)
