# CAPABILITY 4: CODE BLOCK

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
class CapabilityFour:
    def __init__(self, frame):
        self.frame = frame
        self.room_list = get_hotel_rooms()       # holds list of rooms objects
        self.room_frames = []                    # holds list of newly created frames (each represent a room)
        # -------------------------------------------------------------------------------------------
        # CREATE AND SET STATIC WIDGETS (title, reload button)

        # create
        title = tk.Label(self.frame, text="HouseKeeping", font=("Times", 30, "bold"))
        reload_button = tk.Button(self.frame, bg="#D9D9D9", text="Reload Tab", font=("Times", 20), padx=15,
                                  command=self.reset_capability)
        # set
        title.grid(row=0, column=0, sticky="W", padx=120)
        reload_button.grid(row=0, column=1)

        # -------------------------------------------------------------------------------------------
        # CREATE ROOM FRAMES (each frame representing each individual room in the hotel)
        for index, room_obj in enumerate(self.room_list):
            # create frame for each room_obj
            room_frame_label = tk.LabelFrame(self.frame, padx=5, pady=5, bg='#C4C4C4')

            # displays rooms with status "dirty" and "occupied" ONLY! (does so by checking status)
            if (room_obj.get_room_status() == "Dirty") or (room_obj.get_room_status() == "Occupied"):
                # +1 to take account of titleLabel being row=0
                room_frame_label.grid(row=index + 1, column=0, sticky="W", padx=50)

            # append all room frames into list (both displayed and not displayed to still have access to them)
            self.room_frames.append(room_frame_label)

        # -------------------------------------------------------------------------------------------
        # CREATE AND SET WIDGETS FOR EACH ROOM FRAME THAT WAS CREATED
        for index, room_obj in enumerate(self.room_list):
            # create labels
            room_num = tk.Label(self.room_frames[index],
                                text=room_obj.get_room_combo_name(),
                                font=("Times", 14, "bold"), bg='#C4C4C4')
            room_status = tk.Label(self.room_frames[index], bg='#C4C4C4',
                                   text="Status: " + room_obj.get_room_status())

            # create variable holder for each of the checkboxes
            bathroom_value = tk.IntVar()
            towels_value = tk.IntVar()
            vacuum_value = tk.IntVar()
            dust_value = tk.IntVar()
            bed_value = tk.IntVar()
            electronic_value = tk.IntVar()

            # create checkboxes
            bathroom = tk.Checkbutton(self.room_frames[index], text="Bathroom", variable=bathroom_value,
                                      bg='#C4C4C4', onvalue=1, offvalue=0)
            towels = tk.Checkbutton(self.room_frames[index], text="Towels", variable=towels_value,
                                    bg='#C4C4C4', onvalue=1, offvalue=0)
            vacuum = tk.Checkbutton(self.room_frames[index], text="Vacuum", variable=vacuum_value,
                                    bg='#C4C4C4', onvalue=1, offvalue=0)
            dust = tk.Checkbutton(self.room_frames[index], text="Dusting", variable=dust_value,
                                  bg='#C4C4C4', onvalue=1, offvalue=0)
            bed = tk.Checkbutton(self.room_frames[index], text="Bed", variable=bed_value,
                                 bg='#C4C4C4', onvalue=1, offvalue=0)
            electronic = tk.Checkbutton(self.room_frames[index], text="Electronic", variable=electronic_value,
                                        bg='#C4C4C4', onvalue=1, offvalue=0)
            # -------------------------------------------------------------------------------------------
            # create button that change room's status
            #   confirm - will check if all boxes are checked, if so, will change room's status to "Available
            #   maintenance - allows user to change room status to  "maintenance" (requirement of iteration 2)
            confirm_button = tk.Button(self.room_frames[index], text="Confirm", padx=25,
                                       command=lambda bathroom=bathroom_value, towels=towels_value,
                                                      vacuum=vacuum_value, dust=dust_value, bed=bed_value,
                                                      electronic=electronic_value, index=index:
                                       self.confirm_button(bathroom, towels, vacuum, dust, bed, electronic, index))
            maintenance_button = tk.Button(self.room_frames[index], text="Maintenance?", padx=25,
                                           command=lambda index=index: self.maintenance_button(index))

            # set all widgets (labels and checkboxes) in individual room's frame
            room_num.grid(row=0, column=0, columnspan=2, pady=10, sticky="W")
            room_status.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="W")
            bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="W")
            towels.grid(row=1, column=2, padx=5, pady=5, sticky="W")
            vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="W")
            dust.grid(row=1, column=3, padx=5, pady=5, sticky="W")
            bed.grid(row=0, column=4, padx=5, pady=5, sticky="W")
            electronic.grid(row=1, column=4, padx=5, pady=5, sticky="W")
            confirm_button.grid(row=2, column=0, padx=5, pady=5)
            maintenance_button.grid(row=2, column=2, columnspan=2, padx=5, pady=5)
    # END OF INITIALIZER

# =================================================================================================================
    # BUTTON WAS CLICK (Confirm button only)
    #   will check if all boxes are checked
    #   if all boxes are checked, room is clean, will ask user if they wish to change room's status to "Available"
    #   if true, performs change_status(), passing in "Available"
    #   if false, does nothing
    def confirm_button(self, bathroom, towels, vacuum, dust, bed, electronic, index):
        if(bathroom.get() == 1 and towels.get() == 1 and vacuum.get() == 1 and
           dust.get() == 1 and bed.get() == 1 and electronic.get() == 1):
            # create popup
            popup = tk.Tk()
            popup.title("Modify?")
            popup.geometry("225x60")
            popup_label = tk.Label(popup,
                                   text="Change room " + self.room_list[index].get_room_num() + " to Available?",
                                   font=("Times", 12))
            # create and set buttons
            yes_button = tk.Button(popup, text="Yes", padx=25,
                                   command=lambda popup=popup, index=index: self.change_status(popup,
                                                                                               index, "Available"))
            no_button = tk.Button(popup, text="No", padx=25, command=popup.destroy)
            popup_label.grid(row=0, column=0, columnspan=2)
            yes_button.grid(row=1, column=0)
            no_button.grid(row=1, column=1)
            popup.mainloop()
        else:
            # not all checkboxes r check, do nothing.
            pass

    # ---------------------------------------------------------------------------------------------------------
    # BUTTON WAS CLICK (Maintenance button only)
    #   will ask user if they wish to change room's status to "Maintenance"
    #   if yes, will perform change_status(), passing in "Maintenance"
    #   if no, does nothing
    def maintenance_button(self, index):
        # create popup
        popup = tk.Tk()
        popup.title("Modify?")
        popup.geometry("225x60")
        popup_label = tk.Label(popup,
                               text="Change room " + self.room_list[index].get_room_num() + " to Maintenance?",
                               font=("Times", 12))
        # create and set buttons
        yes_button = tk.Button(popup, text="Yes", padx=25,
                               command=lambda popup=popup, index=index: self.change_status(popup,
                                                                                           index, "Maintenance"))
        no_button = tk.Button(popup, text="No", padx=25, command=popup.destroy)
        popup_label.grid(row=0, column=0, columnspan=2)
        yes_button.grid(row=1, column=0)
        no_button.grid(row=1, column=1)
        popup.mainloop()

    # ---------------------------------------------------------------------------------------------------------
    # USER CLICK "Yes" (changes room's status)
    #   update the room's status to "Available" or "Maintenance" based on which button was press
    #   performs rest_capability()
    def change_status(self, popup, index, status):
        # change room status
        new_status = status
        self.room_list[index].set_room_status(new_status)
        update_room(index, new_status)
        print("Room {0} set to status {1}".format(self.room_list[index].get_room_num(),
                                                  self.room_list[index].get_room_status()))
        # destroy popup
        popup.destroy()
        # reset capability
        self.reset_capability()

    # ---------------------------------------------------------------------------------------------------------
    # RESET THE TAB (by destroying it and re-initializing the capability)
    #   only runs after capability modify a room's status
    #   or user click on reload button, manually resetting tab
    def reset_capability(self):
        print("Reload Frame!")
        # destroy all widgets in capability 4
        for widget in self.frame.winfo_children():
            widget.destroy()

        # delete unnecessary variables
        del self.room_list
        del self.room_frames
        # re-initialize capability 4
        CapabilityFour(self.frame)
