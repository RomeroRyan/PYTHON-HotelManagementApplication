# CAPABILITY 1: CODE BLOCK

from rooms_manager import update_room, get_hotel_rooms

try:
    import Tkinter as tk
    import ttk
except ImportError:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")

# =================================================================================================================
class CapabilityOne:
    def __init__(self, frame, tabs, guest_page):
        self.frame = frame
        self.room_list = get_hotel_rooms()
        self.tabs = tabs
        self.guest_page = guest_page
        self.room_buttons = []

        # CAPABILITY 1: initialize static labels (title and description)
        title = tk.Label(self.frame, text="Room Status", font=("Times", 30, "bold"))
        text = tk.Label(self.frame, text="Dirty = yellow \nOccupied = orange \nMaintenance = red", font=("Times", 12))

        # CAPABILITY 1: set labels & buttons
        title.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)


        # CAPABILITY 1: initialize buttons for every room in the hotel
        for index, room in enumerate(self.room_list):
            room_button = tk.Button(self.frame, text=room.get_room_combo_name(), font=("Times", 20), padx=25, command=lambda index=index: self.change_room_status(index))
            room_button.config(bg=self.room_list[index].get_room_color())
            room_button.grid(row=2 + int(index/4), column=index%4, padx=15, pady=15)
            self.room_buttons.append(room_button)

    # =========================================================================================================
    # CAPABILITY 1: button actions

    # WHAT CODE BLOCK DOES: depends on room's status:
    #   if room is Available, goes to Capability 6, allowing user to register a guest
    #   if room is Occupied, goes to capability 6, displaying guest's information in room
    #   if room is Dirty or Maintenance, goes to "switch_to_available" action
    def change_room_status(self, n):
        if self.room_list[n].get_room_status() == "Available":
            self.tabs.select(self.guest_page)
        elif self.room_list[n].get_room_status() == "Occupied":
            tabs.select(self.guest_page)
        elif self.room_list[n].get_room_status() == "Dirty":
            self.switch_to_available(n)
        elif self.room_list[n].get_room_status() == "Maintenance":
            self.switch_to_available(n)

    def change_available(self, popup, room_index):
        status = "Available"
        self.room_list[room_index].set_room_status(status)
        update_room(room_index, status)
        self.room_buttons[room_index].config(bg="#D9D9D9")
        print("Room {0} set to status {1}".format(self.room_list[room_index].get_room_num(), self.room_list[room_index].get_room_status()))
        popup.destroy()

    # WHAT CODE BLOCK DOES: opens a pop-up window, warning the user of the room's current status
    #   User is ask if they wish to change room status to "Available" with yes/no buttons
    def switch_to_available(self, n):
        # creates popup window
        popup = tk.Tk()
        popup.title("WARNING!")
        popup.geometry("250x75")
        popup_label = tk.Label(popup,
                                text="Room " + self.room_list[n].get_room_num() +
                                    " current status:  " + self.room_list[n].get_room_status() +
                                    "\nChange status to Available?",
                                font=("Times", 12), )
        yes_button = tk.Button(popup, text="Yes", padx=25, command=lambda popup=popup, n=n: self.change_available(popup, n))
        no_button = tk.Button(popup, text="No", padx=25, command=popup.destroy)
        popup_label.grid(row=0, column=0, columnspan=2)
        yes_button.grid(row=1, column=0)
        no_button.grid(row=1, column=1)
        popup.mainloop()
