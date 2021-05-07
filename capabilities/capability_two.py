from rooms_manager import get_hotel_rooms
from guest_manager import get_guest_by_room_and_day

try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class CapabilityTwo:
    def __init__(self, frame, notebook, stay_frame):
        self.frame = frame
        self.notebook = notebook
        self.stay_frame = stay_frame
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
            day.grid(row = 2, column = index % len(days), padx=15, pady=5)

        for i, room in enumerate(self.rooms):
            for j in range(len(days)):
                color = room.get_room_color(j)
                room_button = tk.Button(self.days_rooms_container, text=room.get_room_combo_name(),
                                         font=("Times", 15, "bold"), bg=color, command=lambda room=room, day=j: self.switch_to_stays(room, day))
                self.room_buttons.append(room_button)
                room_button.grid(row = 3 + i, column = j % len(days), padx=15, pady=5)
        
        self.days_rooms_container.pack()

    def clear_and_set(self, widget_name, text):
        self.stay_frame.nametowidget(widget_name).config(text=text)

    def switch_to_stays(self, room, day):

        guest = get_guest_by_room_and_day(room, day)

        if guest is None:
            self.clear_and_set("name", "")
            self.clear_and_set("check_in", "")
            self.clear_and_set("check_out", "")
            self.clear_and_set("rate", "")
            self.clear_and_set("total", "")
            self.clear_and_set("paid", "")
            self.clear_and_set("remain", "")
            
            self.notebook.select(5)
        else:
            self.clear_and_set("name", guest.fname + " " + guest.lname)
            self.clear_and_set("check_in", guest.chk_in)
            self.clear_and_set("check_out", guest.chk_out)
            self.clear_and_set("rate", "$10")
            self.clear_and_set("total", "$110")
            self.clear_and_set("paid", "$100")
            self.clear_and_set("remain", "$10")

            self.notebook.select(5)
