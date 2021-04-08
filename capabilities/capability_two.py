from random import *

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class CapabilityTwo:
    def __init__(self, frame):
        weekly_reservation_title = tk.Label(frame, text="Weekly Room Reservations", font=("Times", 20, "bold"))
        weekly_reservation_title.grid(row = 1, column = 3, padx=15, pady=15)

        colors = {
            0: "orange",
            1: "white"
        }

        day_labels = []
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        for day in days:
            day_labels.append(tk.Label(frame, text=day, font=("Times", 20, "bold")))

        for index, day in enumerate(day_labels):
            day.grid(row = 2, column = index % 7, padx=15, pady=15)

        room_buttons = []
        for i in range(0, 56):
            room_buttons.append(tk.Button(frame, text="Room " + str(i+1), font=("Times", 20, "bold"), bg= colors[randint(0, 1)]))

        row = 0
        front = 1
        back = 0

        sizes = {
            0: "K",
            1: "DQ",
            2: "DQk",
            3: "S"
        }

        for index, room in enumerate(room_buttons):
            if index%7 == 0:
                row += 1
                back += 1
            if back % 5 == 0:
                back = 1
                front += 1
            room['text'] = "Room " + str(front) + "0" + str(back) + "(" + sizes[back-1] + ")"
            room.grid(row = row + 3, column = index % 7, padx=15, pady=15)