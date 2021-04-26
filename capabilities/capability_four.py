# CAPABILITY 4: CODE BLOCK

from rooms_manager import get_hotel_rooms

try:
    import Tkinter as tk
    import ttk
except ImportError:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")


class CapabilityFour:
    def __init__(self, frame):
        self.frame = frame
        self.room_list = get_hotel_rooms()
        self.sizeofList = len(self.room_list)       # numerical value of room list
        self.roomFrames = []                        # holds list of newly created frames in this capability
        room_frame_index = 0
        room_widget_index = 0

        # CAPABILITY 4: create and set title label
        title = tk.Label(self.frame, text="Room Status", font=("Times", 30, "bold"))
        title.grid(row=0, column=0, sticky="W", padx=120)

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create frames for each individual room (add it to list roomFrames)
        while room_frame_index < self.sizeofList:
            room = tk.LabelFrame(self.frame, padx=5, pady=5, bg='#C4C4C4')

            # displays rooms with status "dirty" and "occupied" ONLY!
            if (self.room_list[room_frame_index].get_room_status() == "Dirty") or (
                    self.room_list[room_frame_index].get_room_status() == "Occupied"):
                # +1 to take account of titleLabel being row=0
                room.grid(row=room_frame_index + 1, column=0, sticky="W", padx=50)

            # append all room frames into list (both displayed and not displayed)
            self.roomFrames.append(room)
            # index increment
            room_frame_index = room_frame_index + 1

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create & sets all widgets for each room frame
        while room_widget_index < self.sizeofList:
            room_num = tk.Label(self.roomFrames[room_widget_index],
                                text=self.room_list[room_widget_index].get_room_combo_name(),
                                font=("Times", 14, "bold"), bg='#C4C4C4')
            room_status = tk.Label(self.roomFrames[room_widget_index], bg='#C4C4C4',
                                   text="Status: " + self.room_list[0].get_room_status())

            # create the variable holder for each of the checkboxes
            bathroom_check = tk.IntVar()
            towels_check = tk.IntVar()
            vacuum_check = tk.IntVar()
            dust_check = tk.IntVar()
            bed_check = tk.IntVar()
            electronic_check = tk.IntVar()

            # create checkboxes
            bathroom = tk.Checkbutton(self.roomFrames[room_widget_index], text="Bathroom",
                                      variable=bathroom_check, bg='#C4C4C4')
            towels = tk.Checkbutton(self.roomFrames[room_widget_index], text="Towels",
                                    variable=towels_check, bg='#C4C4C4')
            vacuum = tk.Checkbutton(self.roomFrames[room_widget_index], text="Vacuum",
                                    variable=vacuum_check, bg='#C4C4C4')
            dust = tk.Checkbutton(self.roomFrames[room_widget_index], text="Dusting",
                                  variable=dust_check, bg='#C4C4C4')
            bed = tk.Checkbutton(self.roomFrames[room_widget_index], text="Bed",
                                 variable=bed_check, bg='#C4C4C4')
            electronic = tk.Checkbutton(self.roomFrames[room_widget_index], text="Electronic",
                                        variable=electronic_check, bg='#C4C4C4')

            # set all widgets (labels and checkboxes) within the room's frame
            room_num.grid(row=0, column=0, columnspan=2, pady=10, sticky="W")
            room_status.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="W")
            bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="W")
            towels.grid(row=1, column=2, padx=5, pady=5, sticky="W")
            vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="W")
            dust.grid(row=1, column=3, padx=5, pady=5, sticky="W")
            bed.grid(row=0, column=4, padx=5, pady=5, sticky="W")
            electronic.grid(row=1, column=4, padx=5, pady=5, sticky="W")
            # index increment
            room_widget_index = room_widget_index + 1
        # ------------------------------------------------------------------------------------------------------

