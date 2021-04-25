# CAPABILITY 1: CODE BLOCK

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
    def __init__(self, frame1, room_list, tabs, frame6):

        # CAPABILITY 1: initialize static labels (title and description)
        title = tk.Label(frame1, text="Room Status", font=("Times", 30, "bold"))
        text = tk.Label(frame1, text="Dirty = yellow \nOccupied = orange \nMaintenance = red", font=("Times", 12))

        # CAPABILITY 1: initialize buttons for every room in the hotel
        room0 = tk.Button(frame1, text="101 (K)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(0))
        if room_list[0].get_room_status() == "Occupied":
            room0.config(bg="#FF8F51")
        elif room_list[0].get_room_status() == "Dirty":
            room0.config(bg="#F8FC3F")
        elif room_list[0].get_room_status() == "Maintenance":
            room0.config(bg="#FD5E5E")

        room1 = tk.Button(frame1, text="102 (DQ)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(1))
        if room_list[1].get_room_status() == "Occupied":
            room1.config(bg="#FF8F51")
        elif room_list[1].get_room_status() == "Dirty":
            room1.config(bg="#F8FC3F")
        elif room_list[1].get_room_status() == "Maintenance":
            room1.config(bg="#FD5E5E")

        room2 = tk.Button(frame1, text="103 (DQk)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(2))
        if room_list[2].get_room_status() == "Occupied":
            room2.config(bg="#FF8F51")
        elif room_list[2].get_room_status() == "Dirty":
            room2.config(bg="#F8FC3F")
        elif room_list[2].get_room_status() == "Maintenance":
            room2.config(bg="#FD5E5E")

        room3 = tk.Button(frame1, text="104 (S)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(3))
        if room_list[3].get_room_status() == "Occupied":
            room3.config(bg="#FF8F51")
        elif room_list[3].get_room_status() == "Dirty":
            room3.config(bg="#F8FC3F")
        elif room_list[3].get_room_status() == "Maintenance":
            room3.config(bg="#FD5E5E")

        room4 = tk.Button(frame1, text="201 (K)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(4))
        if room_list[4].get_room_status() == "Occupied":
            room4.config(bg="#FF8F51")
        elif room_list[4].get_room_status() == "Dirty":
            room4.config(bg="#F8FC3F")
        elif room_list[4].get_room_status() == "Maintenance":
            room4.config(bg="#FD5E5E")

        room5 = tk.Button(frame1, text="202 (DQ)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(5))
        if room_list[5].get_room_status() == "Occupied":
            room5.config(bg="#FF8F51")
        elif room_list[5].get_room_status() == "Dirty":
            room5.config(bg="#F8FC3F")
        elif room_list[5].get_room_status() == "Maintenance":
            room5.config(bg="#FD5E5E")

        room6 = tk.Button(frame1, text="203 (DQk)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(6))
        if room_list[6].get_room_status() == "Occupied":
            room6.config(bg="#FF8F51")
        elif room_list[6].get_room_status() == "Dirty":
            room6.config(bg="#F8FC3F")
        elif room_list[6].get_room_status() == "Maintenance":
            room6.config(bg="#FD5E5E")

        room7 = tk.Button(frame1, text="204 (S)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(7))
        if room_list[7].get_room_status() == "Occupied":
            room7.config(bg="#FF8F51")
        elif room_list[7].get_room_status() == "Dirty":
            room7.config(bg="#F8FC3F")
        elif room_list[7].get_room_status() == "Maintenance":
            room7.config(bg="#FD5E5E")

        room8 = tk.Button(frame1, text="301 (K)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(8))
        if room_list[8].get_room_status() == "Occupied":
            room8.config(bg="#FF8F51")
        elif room_list[8].get_room_status() == "Dirty":
            room8.config(bg="#F8FC3F")
        elif room_list[8].get_room_status() == "Maintenance":
            room8.config(bg="#FD5E5E")

        room9 = tk.Button(frame1, text="302 (DQ)", font=("Times", 20),
                          padx=25, command=lambda: change_room_status(9))
        if room_list[9].get_room_status() == "Occupied":
            room9.config(bg="#FF8F51")
        elif room_list[9].get_room_status() == "Dirty":
            room9.config(bg="#F8FC3F")
        elif room_list[9].get_room_status() == "Maintenance":
            room9.config(bg="#FD5E5E")

        room10 = tk.Button(frame1, text="303 (DQk)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(10))
        if room_list[10].get_room_status() == "Occupied":
            room10.config(bg="#FF8F51")
        elif room_list[10].get_room_status() == "Dirty":
            room10.config(bg="#F8FC3F")
        elif room_list[10].get_room_status() == "Maintenance":
            room10.config(bg="#FD5E5E")

        room11 = tk.Button(frame1, text="304 (S)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(11))
        if room_list[11].get_room_status() == "Occupied":
            room11.config(bg="#FF8F51")
        elif room_list[11].get_room_status() == "Dirty":
            room11.config(bg="#F8FC3F")
        elif room_list[11].get_room_status() == "Maintenance":
            room11.config(bg="#FD5E5E")

        room12 = tk.Button(frame1, text="401 (K)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(12))
        if room_list[12].get_room_status() == "Occupied":
            room12.config(bg="#FF8F51")
        elif room_list[12].get_room_status() == "Dirty":
            room12.config(bg="#F8FC3F")
        elif room_list[12].get_room_status() == "Maintenance":
            room12.config(bg="#FD5E5E")

        room13 = tk.Button(frame1, text="402 (DQ)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(13))
        if room_list[13].get_room_status() == "Occupied":
            room13.config(bg="#FF8F51")
        elif room_list[13].get_room_status() == "Dirty":
            room13.config(bg="#F8FC3F")
        elif room_list[13].get_room_status() == "Maintenance":
            room13.config(bg="#FD5E5E")

        room14 = tk.Button(frame1, text="403 (DQk)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(14))
        if room_list[14].get_room_status() == "Occupied":
            room14.config(bg="#FF8F51")
        elif room_list[14].get_room_status() == "Dirty":
            room14.config(bg="#F8FC3F")
        elif room_list[14].get_room_status() == "Maintenance":
            room14.config(bg="#FD5E5E")

        room15 = tk.Button(frame1, text="404 (S)", font=("Times", 20),
                           padx=25, command=lambda: change_room_status(15))
        if room_list[15].get_room_status() == "Occupied":
            room15.config(bg="#FF8F51")
        elif room_list[15].get_room_status() == "Dirty":
            room15.config(bg="#F8FC3F")
        elif room_list[15].get_room_status() == "Maintenance":
            room15.config(bg="#FD5E5E")

        # CAPABILITY 1: set labels & buttons
        title.grid(row=0, column=1, columnspan=2, padx=5, pady=5)
        text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        room0.grid(row=2, column=0, padx=15, pady=15)
        room1.grid(row=2, column=1, padx=15, pady=15)
        room2.grid(row=2, column=2, padx=15, pady=15)
        room3.grid(row=2, column=3, padx=15, pady=15)
        room4.grid(row=3, column=0, padx=15, pady=15)
        room5.grid(row=3, column=1, padx=15, pady=15)
        room6.grid(row=3, column=2, padx=15, pady=15)
        room7.grid(row=3, column=3, padx=15, pady=15)
        room8.grid(row=4, column=0, padx=15, pady=15)
        room9.grid(row=4, column=1, padx=15, pady=15)
        room10.grid(row=4, column=2, padx=15, pady=15)
        room11.grid(row=4, column=3, padx=15, pady=15)
        room12.grid(row=5, column=0, padx=15, pady=15)
        room13.grid(row=5, column=1, padx=15, pady=15)
        room14.grid(row=5, column=2, padx=15, pady=15)
        room15.grid(row=5, column=3, padx=15, pady=15)

        # =========================================================================================================
        # CAPABILITY 1: button actions

        # WHAT CODE BLOCK DOES: depends on room's status:
        #   if room is Available, goes to Capability 6, allowing user to register a guest
        #   if room is Occupied, goes to capability 6, displaying guest's information in room
        #   if room is Dirty or Maintenance, goes to "switch_to_available" action
        def change_room_status(n):
            if room_list[n].get_room_status() == "Available":
                tabs.select(frame6)
            elif room_list[n].get_room_status() == "Occupied":
                tabs.select(frame6)
            elif room_list[n].get_room_status() == "Dirty":
                switch_to_available(n)
            elif room_list[n].get_room_status() == "Maintenance":
                switch_to_available(n)

        # ---------------------------------------------

        # WHAT CODE BLOCK DOES: opens a pop-up window, warning the user of the room's current status
        #   User is ask if they wish to change room status to "Available" with yes/no buttons
        def switch_to_available(n):

            # if user clicks yes, this action is perform
            def to_available(a):
                room_list[a].set_room_status("Available")
                print(room_list[a].get_room_status())
                popup.destroy()

            # creates popup window
            popup = tk.Tk()
            popup.title("WARNING!")
            popup.geometry("250x75")
            popupLabel = tk.Label(popup,
                                  text="Room " + room_list[n].get_room_num() +
                                       " current status:  " + room_list[n].get_room_status() +
                                       "\nChange status to Available?",
                                  font=("Times", 12), )
            yesButton = tk.Button(popup, text="Yes", padx=25, command=lambda: to_available(n))
            noButton = tk.Button(popup, text="No", padx=25, command=popup.destroy)
            popupLabel.grid(row=0, column=0, columnspan=2)
            yesButton.grid(row=1, column=0)
            noButton.grid(row=1, column=1)
            popup.mainloop()
