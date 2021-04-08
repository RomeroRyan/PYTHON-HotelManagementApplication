try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class CapabilityThree:
    def __init__(self, frame):
        self.frame = frame
        guest_registration_title = tk.Label(frame, text="Guest Registration", font=("Times", 20, "bold"))
        guest_registration_title.grid(row = 1, column = 3, padx=15, pady=15)

        first_name = tk.Label(frame, text="First Name", font=("Times", 20, "bold"))
        first_name.grid(row = 2, column = 1, padx=15, pady=15)
        first_name_entry = tk.Entry(frame, font=("Times", 20, "bold"))
        first_name_entry.grid(row = 2, column = 2, padx=15, pady=15)

        last_name = tk.Label(frame, text="Last Name", font=("Times", 20, "bold"))
        last_name.grid(row = 3, column = 1, padx=15, pady=15)
        last_name_entry = tk.Entry(frame, font=("Times", 20, "bold"))
        last_name_entry.grid(row = 3, column = 2, padx=15, pady=15)

        check_in = tk.Label(frame, text="Check-In", font=("Times", 20, "bold"))
        check_in.grid(row = 4, column = 1, padx=15, pady=15)
        check_in_entry = tk.Entry(frame, font=("Times", 20, "bold"))
        check_in_entry.grid(row = 4, column = 2, padx=15, pady=15)

        check_out = tk.Label(frame, text="Check Out", font=("Times", 20, "bold"))
        check_out.grid(row = 5, column = 1, padx=15, pady=15)
        check_out_entry = tk.Entry(frame, font=("Times", 20, "bold"))
        check_out_entry.grid(row = 5, column = 2, padx=15, pady=15)

        room_type = tk.Label(frame, text="Room Type", font=("Times", 20, "bold"))
        room_type.grid(row = 6, column = 1, padx=15, pady=15)
        room_type_entry = tk.Entry(frame, font=("Times", 20, "bold"))
        room_type_entry.grid(row = 6, column = 2, padx=15, pady=15)


        check_availability = tk.Button(frame, text="Check Availability")
        check_availability.grid(row = 7, column = 1, padx=15, pady=15)

        # Fixed values for now
        daily_rate = tk.Label(frame, text="Daily Rate", font=("Times", 20, "bold"))
        daily_rate.grid(row = 8, column = 1, padx=15, pady=15)
        daily_rate_value = tk.Label(frame, text="$30", font=("Times", 15))
        daily_rate_value.grid(row = 9, column = 1, padx=15, pady=15)

        total_charge = tk.Label(frame, text="Total Charge", font=("Times", 20, "bold"))
        total_charge.grid(row = 8, column = 2, padx=15, pady=15)
        total_charge_value = tk.Label(frame, text="$200", font=("Times", 15))
        total_charge_value.grid(row = 9, column = 2, padx=15, pady=15)

        check_reservations = tk.Button(frame, text="Show Reservations", command=self.show_reservations)
        check_reservations.grid(row = 11, column = 3, padx=15, pady=15)

    def show_guest_reservation(self):
        win = tk.Toplevel()
        win.wm_title("Guest Reservations")
        group = tk.LabelFrame(win, text="Rooms", font=("Times", 20, "bold"))

        first_name = tk.Label(group, text="First Name", font=("Times", 20, "bold"))
        first_name.grid(row = 1, column = 1, padx=2, pady=2)
        first_name_label = tk.Label(group, text="Jacob", font=("Times", 15))
        first_name_label.grid(row = 2, column = 1, padx=2, pady=2)

        last_name = tk.Label(group, text="Last Name", font=("Times", 20, "bold"))
        last_name.grid(row = 3, column = 1, padx=2, pady=2)
        last_name_label = tk.Label(group, text="Powell", font=("Times", 15))
        last_name_label.grid(row = 4, column = 1, padx=2, pady=2)

        check_in = tk.Label(group, text="Check-In", font=("Times", 20, "bold"))
        check_in.grid(row = 5, column = 1, padx=2, pady=2)
        check_in_label = tk.Label(group, text="10/24/16", font=("Times", 15))
        check_in_label.grid(row = 6, column = 1, padx=2, pady=2)

        check_out = tk.Label(group, text="Check Out", font=("Times", 20, "bold"))
        check_out.grid(row = 7, column = 1, padx=2, pady=2)
        check_out_label = tk.Label(group, text="10/31/16", font=("Times", 15))
        check_out_label.grid(row = 8, column = 1, padx=2, pady=2)

        room_type = tk.Label(group, text="Room Type", font=("Times", 20, "bold"))
        room_type.grid(row = 9, column = 1, padx=2, pady=2)
        room_type_label = tk.Label(group, text="DQ", font=("Times", 15))
        room_type_label.grid(row = 10, column = 1, padx=2, pady=2)

        # Fixed values for now
        daily_rate = tk.Label(group, text="Daily Rate", font=("Times", 20, "bold"))
        daily_rate.grid(row = 11, column = 1, padx=2, pady=2)
        daily_rate_value = tk.Label(group, text="$30", font=("Times", 15))
        daily_rate_value.grid(row = 12, column = 1, padx=2, pady=2)

        total_charge = tk.Label(group, text="Total Charge", font=("Times", 20, "bold"))
        total_charge.grid(row = 13, column = 1, padx=2, pady=2)
        total_charge_value = tk.Label(group, text="$210", font=("Times", 15))
        total_charge_value.grid(row = 14, column = 1, padx=2, pady=2)

        group.grid(row = 12, column = 7, padx=2, pady=2)

    def show_reservations(self):
        win = tk.Toplevel()
        win.wm_title("Show Reservations")
        rooms = []
        group = tk.LabelFrame(win, text="Rooms", font=("Times", 20, "bold"))
        for i in range(3):
            rooms.append(tk.Button(group, text="Room " + str(i+1) + "0" + str(i), font=("Times", 20, "bold"), bg="orange", command=self.show_guest_reservation))
            rooms[i].grid(row = i, column = 1, padx=15, pady=15)
        group.grid(row = 1, column = 1, padx=15, pady=15)