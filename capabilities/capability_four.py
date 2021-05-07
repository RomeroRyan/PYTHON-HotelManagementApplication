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

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create and set title label
        title = tk.Label(self.frame, text="HouseKeeping", font=("Times", 30, "bold"))
        title.grid(row=0, column=0, sticky="W", padx=120)

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create frames for each individual room (add it to list room_frames)
        for index, room_obj in enumerate(self.room_list):
            # create frame for each room_obj
            room_frame_label = tk.LabelFrame(self.frame, padx=5, pady=5, bg='#C4C4C4')

            # displays rooms with status "dirty" and "occupied" ONLY! (does so by checking status)
            if (room_obj.get_room_status() == "Dirty") or (room_obj.get_room_status() == "Occupied"):
                # +1 to take account of titleLabel being row=0
                room_frame_label.grid(row=index + 1, column=0, sticky="W", padx=50)

            # append all room frames into list (both displayed and not displayed to still have access to them)
            self.room_frames.append(room_frame_label)

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create & sets widgets for each room frame that was created
        for index, room_obj in enumerate(self.room_list):
            # creat label for room number and room status
            room_num = tk.Label(self.room_frames[index],
                                text=room_obj.get_room_combo_name(),
                                font=("Times", 14, "bold"), bg='#C4C4C4')
            room_status = tk.Label(self.room_frames[index], bg='#C4C4C4',
                                   text="Status: " + room_obj.get_room_status())

            # create variable holder for each of the checkboxes
            bathroom_check = tk.IntVar()
            towels_check = tk.IntVar()
            vacuum_check = tk.IntVar()
            dust_check = tk.IntVar()
            bed_check = tk.IntVar()
            electronic_check = tk.IntVar()

            # create checkboxes
            bathroom = tk.Checkbutton(self.room_frames[index], text="Bathroom", variable=bathroom_check,
                                      bg='#C4C4C4', onvalue=1, offvalue=0)
            towels = tk.Checkbutton(self.room_frames[index], text="Towels", variable=towels_check,
                                    bg='#C4C4C4', onvalue=1, offvalue=0)
            vacuum = tk.Checkbutton(self.room_frames[index], text="Vacuum", variable=vacuum_check,
                                    bg='#C4C4C4', onvalue=1, offvalue=0)
            dust = tk.Checkbutton(self.room_frames[index], text="Dusting", variable=dust_check,
                                  bg='#C4C4C4', onvalue=1, offvalue=0)
            bed = tk.Checkbutton(self.room_frames[index], text="Bed", variable=bed_check,
                                 bg='#C4C4C4', onvalue=1, offvalue=0)
            electronic = tk.Checkbutton(self.room_frames[index], text="Electronic", variable=electronic_check,
                                        bg='#C4C4C4', onvalue=1, offvalue=0)
            # -------------------------------------------------------------------------------------------
            # create button that change room's status
            #   confirm - will check if all boxes are checked, if so, will change room's status to "Available
            #   maintenance - allows user to change room status to  "maintenance" (requirement of iteration 2)
            confirm_button = tk.Button(self.room_frames[index], text="Confirm", padx=25,
                                    command=lambda bathroom=bathroom_check, towels=towels_check, vacuum=vacuum_check,
                                                   dust=dust_check, bed=bed_check, electronic=electronic_check,
                                                   index=index: self.confirm_button(bathroom, towels, vacuum, dust,
                                                                                   bed, electronic, index))
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
    # =========================================================================================================
    # CAPABILITY 4: button action (confirm button only)
    #   will check if all boxes are checked
    #   if all boxes are checked, room is clean, will ask user if they wish to change room's status to "Available"
    #       if yes, will update room's status with function call change_status()
    #   if not all boxes are checked, does nothing
    def confirm_button(self, bathroom, towels, vacuum, dust, bed, electronic, index):
        if(bathroom.get() == 1 and towels.get() == 1 and vacuum.get() == 1 and
           dust.get() == 1 and bed.get() == 1 and electronic.get() == 1):
            print("All are checked!")
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

    # =========================================================================================================
    # CAPABILITY 4: button action (maintenance button only)
    #   will ask user if they wish to change room's status to "Maintenance"
    #   if yes, will update room's status with function call change_status()
    #   if no, does nothing
    def maintenance_button(self, index):
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

    # =========================================================================================================
    # CAPABILITY 4: user has click yes on updating status on either Confirm or Maintenance button
    #   will update the room status with the status string that was passed in
    #   delete all widgets and variables and re-initialize capability 4
    def change_status(self, popup, index, status):
        # change room status
        new_status = status
        self.room_list[index].set_room_status(new_status)
        update_room(index, new_status)
        print("Room {0} set to status {1}".format(self.room_list[index].get_room_num(),
                                                  self.room_list[index].get_room_status()))
        # destroy popup
        popup.destroy()

        # destroy all widgets in capability 4
        for widget in self.frame.winfo_children():
            widget.destroy()

        # delete unnecessary variables
        del self.room_list
        del self.room_frames
        # re-initialize capability 4
        CapabilityFour(self.frame)

