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
        self.room_frames = []                        # holds list of newly created frames in this capability
        
        # CAPABILITY 4: create and set title label
        title = tk.Label(self.frame, text="Room Status", font=("Times", 30, "bold"))
        title.grid(row=0, column=0, sticky="W", padx=120)

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create frames for each individual room (add it to list room_frames)
        for index, room_obj in enumerate(self.room_list):
            room_frame_label = tk.LabelFrame(self.frame, padx=5, pady=5, bg='#C4C4C4')

            # displays rooms with status "dirty" and "occupied" ONLY!
            if (room_obj.get_room_status() == "Dirty") or (room_obj.get_room_status() == "Occupied"):
                # +1 to take account of titleLabel being row=0
                room_frame_label.grid(row=index + 1, column=0, sticky="W", padx=50)

            # append all room frames into list (both displayed and not displayed)
            self.room_frames.append(room_frame_label)

        # ----------------------------------------------------------------------------
        # CAPABILITY 4: create & sets all widgets for each room frame
        for index, room_obj in enumerate(self.room_list):
            room_num = tk.Label(self.room_frames[index],
                                text=room_obj.get_room_combo_name(),
                                font=("Times", 14, "bold"), bg='#C4C4C4')
            room_status = tk.Label(self.room_frames[index], bg='#C4C4C4',
                                   text="Status: " + room_obj.get_room_status())

            # create the variable holder for each of the checkboxes
            bathroom_check = tk.IntVar()
            towels_check = tk.IntVar()
            vacuum_check = tk.IntVar()
            dust_check = tk.IntVar()
            bed_check = tk.IntVar()
            electronic_check = tk.IntVar()

            # create checkboxes
            bathroom = tk.Checkbutton(self.room_frames[index], text="Bathroom",
                                      variable=bathroom_check, bg='#C4C4C4')
            towels = tk.Checkbutton(self.room_frames[index], text="Towels",
                                    variable=towels_check, bg='#C4C4C4')
            vacuum = tk.Checkbutton(self.room_frames[index], text="Vacuum",
                                    variable=vacuum_check, bg='#C4C4C4')
            dust = tk.Checkbutton(self.room_frames[index], text="Dusting",
                                  variable=dust_check, bg='#C4C4C4')
            bed = tk.Checkbutton(self.room_frames[index], text="Bed",
                                 variable=bed_check, bg='#C4C4C4')
            electronic = tk.Checkbutton(self.room_frames[index], text="Electronic",
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
        # ------------------------------------------------------------------------------------------------------

