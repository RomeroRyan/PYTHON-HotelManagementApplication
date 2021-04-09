import tkinter as tk

# Guest Profile
class CapabilitySix:
    def __init__(self, frame): 
        title_label = tk.Label(frame, text="Current Guest Show Screen", bg= 'steel blue')
        title_label.grid(row=0, column = 0, columnspan =1)

        gname_label = tk.Label(frame, text="Guest Name:")
        gname_label.grid(row=1, column = 0)

        checkin_label = tk.Label(frame, text="Check-in Date:")
        checkin_label.grid(row=2, column = 0)

        checkout_label = tk.Label(frame, text="Check-out Date:")
        checkout_label.grid(row=3, column = 0)

        roomrate_label = tk.Label(frame, text="Room rate:")
        roomrate_label.grid(row=4, column = 0)

        total_label = tk.Label(frame, text="Total Charge:")
        total_label.grid(row=5, column = 0)

        paid_label = tk.Label(frame, text="Payment Made:")
        paid_label.grid(row=6, column = 0)

        remain_label = tk.Label(frame, text="Balance:")
        remain_label.grid(row=7, column = 0)

        gname = tk.Label(frame, width=30, text="John Win",bg='#C4C4C4')
        gname.grid(row=1, column=1, padx=20)

        checkin = tk.Label(frame, width=30, text="03/26/2021",bg='#C4C4C4')
        checkin.grid(row=2, column=1)

        checkout = tk.Label(frame, width=30, text="03/30/2021",bg='#C4C4C4')
        checkout.grid(row=3, column=1)

        roomrate = tk.Label(frame, width=30, text="$100/night",bg='#C4C4C4')
        roomrate.grid(row=4, column=1)

        total = tk.Label(frame, width=30, text = "$ 400",bg='#C4C4C4')
        total.grid(row=5, column=1)

        paid = tk.Label(frame, width=30, text = "$ 150",bg='#C4C4C4')
        paid.grid(row=6, column=1)

        remain = tk.Label(frame, width=30, text = "$ 250", bg='#C4C4C4')
        remain.grid(row=7, column=1)
