# CAPABILITY 4: CODE BLOCK
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
    def __init__(self, frame4):

        # CAPABILITY 4: create title widgets
        capa4Title = tk.Label(frame4, text="Room Status", font=("Times", 20, "bold"))

        # CAPABILITY 4: create individual room frames
        capa4Room02 = tk.LabelFrame(frame4, padx=5, pady=5, bg='#C4C4C4')
        capa4Room04 = tk.LabelFrame(frame4, padx=5, pady=5, bg='#C4C4C4')
        capa4Room12 = tk.LabelFrame(frame4, padx=5, pady=5, bg='#C4C4C4')
        capa4Room14 = tk.LabelFrame(frame4, padx=5, pady=5, bg='#C4C4C4')

        # CAPABILITY 4: create label widgets for each individual room frame

        # create room 2 labels
        room02Number = tk.Label(capa4Room02, text="102 (DQ)", font=("Times", 14, "bold"), bg='#C4C4C4')
        room02Housekeeper = tk.Label(capa4Room02, text="HouseKeeper: John D.", bg='#C4C4C4')
        room02Status = tk.Label(capa4Room02, text="Status: Dirty", bg='#C4C4C4')
        room02Bathroom = tk.Label(capa4Room02, text="Bathroom: To Do", bg='#C4C4C4')
        room02Towels = tk.Label(capa4Room02, text="Towels: Done", bg='#C4C4C4')
        room02Vacuum = tk.Label(capa4Room02, text="Vacuum: To Do", bg='#C4C4C4')
        room02Dusting = tk.Label(capa4Room02, text="Dusting: Done", bg='#C4C4C4')
        room02Bed = tk.Label(capa4Room02, text="Beds: To Do", bg='#C4C4C4')
        room02Electronics = tk.Label(capa4Room02, text="Electronics: To Do", bg='#C4C4C4')

        # create room 4 labels
        room04Number = tk.Label(capa4Room04, text="104 (S)", font=("Times", 14, "bold"), bg='#C4C4C4')
        room04Housekeeper = tk.Label(capa4Room04, text="HouseKeeper: Anna M.", bg='#C4C4C4')
        room04Status = tk.Label(capa4Room04, text="Status: Dirty", bg='#C4C4C4')
        room04Bathroom = tk.Label(capa4Room04, text="Bathroom: Done", bg='#C4C4C4')
        room04Towels = tk.Label(capa4Room04, text="Towels: Done", bg='#C4C4C4')
        room04Vacuum = tk.Label(capa4Room04, text="Vacuum: To Do", bg='#C4C4C4')
        room04Dusting = tk.Label(capa4Room04, text="Dusting: Done", bg='#C4C4C4')
        room04Bed = tk.Label(capa4Room04, text="Beds: To Do", bg='#C4C4C4')
        room04Electronics = tk.Label(capa4Room04, text="Electronics: To Do", bg='#C4C4C4')

        # create room 12 labels
        room12Number = tk.Label(capa4Room12, text="304 (S)", font=("Times", 14, "bold"), bg='#C4C4C4')
        room12Housekeeper = tk.Label(capa4Room12, text="HouseKeeper: John D.", bg='#C4C4C4')
        room12Status = tk.Label(capa4Room12, text="Status: Dirty", bg='#C4C4C4')
        room12Bathroom = tk.Label(capa4Room12, text="Bathroom: To Do", bg='#C4C4C4')
        room12Towels = tk.Label(capa4Room12, text="Towels: Done", bg='#C4C4C4')
        room12Vacuum = tk.Label(capa4Room12, text="Vacuum: To Do", bg='#C4C4C4')
        room12Dusting = tk.Label(capa4Room12, text="Dusting: Done", bg='#C4C4C4')
        room12Bed = tk.Label(capa4Room12, text="Beds: To Do", bg='#C4C4C4')
        room12Electronics = tk.Label(capa4Room12, text="Electronics: To Do", bg='#C4C4C4')

        # create room 14 labels
        room14Number = tk.Label(capa4Room14, text="402 (DQ)", font=("Times", 14, "bold"), bg='#C4C4C4')
        room14Housekeeper = tk.Label(capa4Room14, text="HouseKeeper: Sam P.", bg='#C4C4C4')
        room14Status = tk.Label(capa4Room14, text="Status: Dirty", bg='#C4C4C4')
        room14Bathroom = tk.Label(capa4Room14, text="Bathroom: To Do", bg='#C4C4C4')
        room14Towels = tk.Label(capa4Room14, text="Towels: To Do", bg='#C4C4C4')
        room14Vacuum = tk.Label(capa4Room14, text="Vacuum: TO Do", bg='#C4C4C4')
        room14Dusting = tk.Label(capa4Room14, text="Dusting: Done", bg='#C4C4C4')
        room14Bed = tk.Label(capa4Room14, text="Beds: Done", bg='#C4C4C4')
        room14Electronics = tk.Label(capa4Room14, text="Electronics: Done", bg='#C4C4C4')

        # CAPABILITY 4: set widgets into individual room frames

        # set room 2 widgets
        room02Number.grid(row=0, column=0, rowspan=2, pady=10, sticky="E")
        room02Status.grid(row=0, column=1, padx=5, pady=5, sticky="E")
        room02Housekeeper.grid(row=1, column=1, padx=5, pady=5, sticky="E")
        room02Bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="E")
        room02Towels.grid(row=1, column=2, padx=5, pady=5, sticky="E")
        room02Vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="E")
        room02Dusting.grid(row=1, column=3, padx=5, pady=5, sticky="E")
        room02Bed.grid(row=0, column=4, padx=5, pady=5, sticky="E")
        room02Electronics.grid(row=1, column=4, padx=5, pady=5, sticky="E")

        # set room 4 widgets
        room04Number.grid(row=0, column=0, rowspan=2, pady=10, sticky="E")
        room04Status.grid(row=0, column=1, padx=5, pady=5, sticky="E")
        room04Housekeeper.grid(row=1, column=1, padx=5, pady=5, sticky="E")
        room04Bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="E")
        room04Towels.grid(row=1, column=2, padx=5, pady=5, sticky="E")
        room04Vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="E")
        room04Dusting.grid(row=1, column=3, padx=5, pady=5, sticky="E")
        room04Bed.grid(row=0, column=4, padx=5, pady=5, sticky="E")
        room04Electronics.grid(row=1, column=4, padx=5, pady=5, sticky="E")

        # set room 12 widgets
        room12Number.grid(row=0, column=0, rowspan=2, pady=10, sticky="E")
        room12Status.grid(row=0, column=1, padx=5, pady=5, sticky="E")
        room12Housekeeper.grid(row=1, column=1, padx=5, pady=5, sticky="E")
        room12Bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="E")
        room12Towels.grid(row=1, column=2, padx=5, pady=5, sticky="E")
        room12Vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="E")
        room12Dusting.grid(row=1, column=3, padx=5, pady=5, sticky="E")
        room12Bed.grid(row=0, column=4, padx=5, pady=5, sticky="E")
        room12Electronics.grid(row=1, column=4, padx=5, pady=5, sticky="E")

        # set room 14 widgets
        room14Number.grid(row=0, column=0, rowspan=2, pady=10, sticky="E")
        room14Status.grid(row=0, column=1, padx=5, pady=5, sticky="E")
        room14Housekeeper.grid(row=1, column=1, padx=5, pady=5, sticky="E")
        room14Bathroom.grid(row=0, column=2, padx=5, pady=5, sticky="E")
        room14Towels.grid(row=1, column=2, padx=5, pady=5, sticky="E")
        room14Vacuum.grid(row=0, column=3, padx=5, pady=5, sticky="E")
        room14Dusting.grid(row=1, column=3, padx=5, pady=5, sticky="E")
        room14Bed.grid(row=0, column=4, padx=5, pady=5, sticky="E")
        room14Electronics.grid(row=1, column=4, padx=5, pady=5, sticky="E")

        # CAPABILITY 4: set frames into Main Frame
        capa4Title.grid(row=0, column=0, sticky="W")
        capa4Room02.grid(row=1, column=0, sticky="W")
        capa4Room04.grid(row=2, column=0, sticky="W")
        capa4Room12.grid(row=3, column=0, sticky="W")
        capa4Room14.grid(row=4, column=0, sticky="W")
