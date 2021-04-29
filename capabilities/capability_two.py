from random import *

from rooms_manager import get_hotel_rooms

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class CapabilityTwo:
    def __init__(self, frame):
        self.frame = frame
        self.title_container = tk.LabelFrame(frame)
        self.days_rooms_container = tk.LabelFrame(frame)
        self.weekly_reservation_title = tk.Label(self.title_container, text="Weekly Room Reservations", font=("Times", 20, "bold"))
        self.weekly_reservation_title.grid(row = 1, column = 3, padx=15, pady=15)
        self.rooms = get_hotel_rooms()
        self.day_labels = []
        self.room_buttons = []
        self.title_container.pack()

        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

        for day in days:
            self.day_labels.append(tk.Label(self.days_rooms_container, text=day, font=("Times", 15, "bold")))

        for index, day in enumerate(self.day_labels):
            day.grid(row = 2, column = index % 7, padx=15, pady=5)

        for i in range(len(self.rooms)):
            for j in range(0, 7):
                color = self.rooms[i].get_room_color(j)
                room_button = tk.Button(self.days_rooms_container, text=self.rooms[i].get_room_combo_name(), font=("Times", 15, "bold"), bg=color)
                self.room_buttons.append(room_button)
                room_button.grid(row = 3 + i, column = j % 7, padx=15, pady=5)

        
        self.days_rooms_container.pack()
