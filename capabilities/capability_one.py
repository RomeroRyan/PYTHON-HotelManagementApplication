# CAPABILITY 1: CODE BLOCK

import datetime
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
# START OF INITIALIZER
class CapabilityOne:
    def __init__(self, frame, tabs, guest_page):
        self.frame = frame
        self.room_list = get_hotel_rooms()
        self.tabs = tabs
        self.guest_page = guest_page        # use to get to capability 6 when a button is click
        self.room_buttons_list = []         # saves the list of buttons, allowing access to them with an index
        # ---------------------------------------------------------------------------------------------------------
        # INITIALIZE AND SET STATIC WIDGETS (title, description, reload button)

        # create labels
        title = tk.Label(self.frame, text="Room Status", font=("Times", 30, "bold"))
        description = tk.Label(self.frame, text="Dirty = yellow \nOccupied = orange \nMaintenance = red",
                               font=("Times", 12))
        # create reload button
        reload_button = tk.Button(self.frame, bg="#D9D9D9", text="Reload Tab", font=("Times", 20), padx=15,
                                  command=self.reset_capability)
        # set labels & button
        title.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        description.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        reload_button.grid(row=1, column=3)
        # ---------------------------------------------------------------------------------------------------------
        # INITIALIZE AND SET ROOM BUTTONS (each button represent a room in the hotel)
        for index, room in enumerate(self.room_list):
            # create button
            room_button = tk.Button(self.frame, text=room.get_room_combo_name(), font=("Times", 20), padx=25,
                                    command=lambda index=index: self.change_room_status(index))
            # reconfigure button color based on status
            room_button.config(bg=self.room_list[index].get_room_color(datetime.datetime.today().weekday()))
            # set button in the frame
            room_button.grid(row=2 + int(index/4), column=index % 4, padx=15, pady=15)
            # append button into room_buttons_list for later access
            self.room_buttons_list.append(room_button)
    # END OF INITIALIZER

# =================================================================================================================
    # BUTTON WAS CLICK (determine what to do after click)
    #   if room is Available, goes to Capability 6, allowing user to register a guest
    #   if room is Occupied, goes to capability 6, displaying guest's information in room
    #   if room is Dirty or Maintenance, performs update_status_check()
    def change_room_status(self, index):
        if self.room_list[index].get_room_status() == "Available":
            self.tabs.select(self.guest_page)           # switches tab to capability 6
        elif self.room_list[index].get_room_status() == "Occupied":
            self.tabs.select(self.guest_page)           # switches tab to capability 6
        elif self.room_list[index].get_room_status() == "Dirty":
            self.update_status_check(index)
        elif self.room_list[index].get_room_status() == "Maintenance":
            self.update_status_check(index)

    # ---------------------------------------------------------------------------------------------------------
    # BUTTON CLICKED WAS ROOM WITH STATUS: "Dirty" or "Maintenance",
    #   User is ask if they wish to change room status to "Available" with yes/no buttons
    #   if User clicks yes, perform change_available()
    #   if User click no, does nothing
    def update_status_check(self, index):
        # creates popup window
        popup = tk.Tk()
        popup.title("WARNING!")
        popup.geometry("250x80")
        popup_label = tk.Label(popup,
                               text="Room " + self.room_list[index].get_room_num() +
                               " current status: " + self.room_list[index].get_room_status() +
                                    "\nChange status to Available?",
                               font=("Times", 12))
        # create and set buttons
        yes_button = tk.Button(popup, text="Yes", padx=25,
                               command=lambda popup=popup, index=index: self.change_available(popup, index))
        no_button = tk.Button(popup, text="No", padx=25, command=popup.destroy)
        popup_label.grid(row=0, column=0, columnspan=2)
        yes_button.grid(row=1, column=0)
        no_button.grid(row=1, column=1)
        popup.mainloop()

    # ---------------------------------------------------------------------------------------------------------
    # USER CLICK "Yes" (changes room's status to "Available")
    #   update the room's status
    #   performs reset_capability()
    def change_available(self, popup, room_index):
        # change status
        status = "Available"
        self.room_list[room_index].set_room_status(status)
        update_room(room_index, status)
        print("Room {0} set to status {1}".format(self.room_list[room_index].get_room_num(),
                                                  self.room_list[room_index].get_room_status()))
        # destroy popup
        popup.destroy()
        # reset capability
        self.reset_capability()

    # ---------------------------------------------------------------------------------------------------------
    # RESET THE TAB (by destroying it and re-initializing the capability)
    #   only runs after capability modify a room's status
    #   or user click on reload button, manually resetting tab
    def reset_capability(self):
        # destroy all widgets in capability 1
        for widget in self.frame.winfo_children():
            widget.destroy()

        # delete unnecessary variables
        del self.room_list
        del self.room_buttons_list
        # re-initialize capability 1
        CapabilityOne(self.frame, self.tabs, self.guest_page)
