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


class CapabilityOne:
    def __init__(self, frame):
        frame1 = frame

        # CAPABILITY 1: create widgets
        capa1Title = tk.Label(frame1, text="Room Status", font=("Times", 20, "bold"))
        capa1Text = tk.Label(frame1, text="Dirty = yellow \nOccupied = orange \nMaintenance = red")

        # CAPABILITY 1: create buttons for every room in the hotel
        capa1Room01 = tk.Button(frame1, text="101 (K)", padx=25)
        capa1Room02 = tk.Button(frame1, text="102 (DQ)", bg="orange", padx=25)
        capa1Room03 = tk.Button(frame1, text="103 (DQk)", padx=25)
        capa1Room04 = tk.Button(frame1, text="104 (S)", bg="orange", padx=25)
        capa1Room05 = tk.Button(frame1, text="201 (K)", padx=25)
        capa1Room06 = tk.Button(frame1, text="202 (DQ)", padx=25)
        capa1Room07 = tk.Button(frame1, text="203 (DQk)", bg="yellow", padx=25)
        capa1Room08 = tk.Button(frame1, text="204 (S)", padx=25)
        capa1Room09 = tk.Button(frame1, text="301 (K)", bg="red", padx=25)
        capa1Room10 = tk.Button(frame1, text="302 (DQ)", padx=25)
        capa1Room11 = tk.Button(frame1, text="303 (DQk)", padx=25)
        capa1Room12 = tk.Button(frame1, text="304 (S)", bg="orange", padx=25)
        capa1Room13 = tk.Button(frame1, text="401 (K)", padx=25)
        capa1Room14 = tk.Button(frame1, text="402 (DQ)", bg="orange", padx=25)
        capa1Room15 = tk.Button(frame1, text="403 (DQk)", bg="yellow", padx=25)
        capa1Room16 = tk.Button(frame1, text="404 (S)", bg="red", padx=25)

        # CAPABILITY 1: set labels
        capa1Title.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        capa1Text.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # CAPABILITY 1: set buttons
        capa1Room01.grid(row=2, column=0, padx=15, pady=15)
        capa1Room02.grid(row=2, column=1, padx=15, pady=15)
        capa1Room03.grid(row=2, column=2, padx=15, pady=15)
        capa1Room04.grid(row=2, column=3, padx=15, pady=15)
        capa1Room05.grid(row=3, column=0, padx=15, pady=15)
        capa1Room06.grid(row=3, column=1, padx=15, pady=15)
        capa1Room07.grid(row=3, column=2, padx=15, pady=15)
        capa1Room08.grid(row=3, column=3, padx=15, pady=15)
        capa1Room09.grid(row=4, column=0, padx=15, pady=15)
        capa1Room10.grid(row=4, column=1, padx=15, pady=15)
        capa1Room11.grid(row=4, column=2, padx=15, pady=15)
        capa1Room12.grid(row=4, column=3, padx=15, pady=15)
        capa1Room13.grid(row=5, column=0, padx=15, pady=15)
        capa1Room14.grid(row=5, column=1, padx=15, pady=15)
        capa1Room15.grid(row=5, column=2, padx=15, pady=15)
        capa1Room16.grid(row=5, column=3, padx=15, pady=15)