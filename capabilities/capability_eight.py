import tkinter as tk

from guest_manager import get_guests
from report_manager import get_report_section

# Report
class CapabilityEight:
    def __init__(self, frame):
        self.guests = get_guests()
        self.frame = frame

        self.checkins = get_report_section("checkins")
        self.checkouts = get_report_section("checkouts")
        
        self.checkin_group = tk.LabelFrame(self.frame, text="Checkins", font=("Times", 20, "bold"))
        self.checkin_group.grid(row=1, column =4)

        self.checkout_group = tk.LabelFrame(self.frame, text="Checkouts", font=("Times", 20, "bold"))
        self.checkout_group.grid(row=2, column =4)

        title_label = tk.Label(frame, text="Today's Report", font=30)
        title_label.grid(row=0, column =4)

        if len(self.checkins) == 0:
            room_label = tk.Label(self.checkin_group, text= "None")
            room_label.grid(row=2, column = 0)

        if len(self.checkouts) == 0:
            room_label = tk.Label(self.checkout_group, text= "None")
            room_label.grid(row=2, column = 1)


        for i, guest in enumerate(self.checkins):
            room_label = tk.Label(self.checkin_group, text= str(i+1) + ". " + guest.rm_number)
            room_label.grid(row=i+2, column = 0)
            guest_label = tk.Label(self.checkin_group, text=guest.fname + " " + guest.lname)
            guest_label.grid(row=i+3, column = 0)

        for i, guest in enumerate(self.checkouts):
            room_label = tk.Label(self.checkout_group, text= str(i+1) + ". " + guest.rm_number)
            room_label.grid(row=i+2, column = 1)
            guest_label = tk.Label(self.checkout_group, text=guest.fname + " " + guest.lname)
            guest_label.grid(row=i+3, column = 1)

        total_label = tk.Label(frame, text="Total: $ 1080")
        total_label.grid(row=99, column = 6)
