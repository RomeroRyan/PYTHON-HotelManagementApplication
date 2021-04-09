import tkinter as tk

class CapabilityEight:
    def __init__(self,frame):

#frame = tk.Tk()
        #frame.title('Report')
#frame.geometry("500x500")

        title_label = tk.Label(frame, text="Today's Report", font=30)
        title_label.grid(row=0, column =4, columnspan =1)

        checkin_label = tk.Label(frame, text="Check-in", bg='#C4C4C4')
        checkin_label.grid(row=1, column = 0)

        room1_label = tk.Label(frame, text="1. Room #303")
        room1_label.grid(row=2, column = 0)
        guest1_label = tk.Label(frame, text="Ben Ho")
        guest1_label.grid(row=3, column = 0)

        room2_label = tk.Label(frame, text="2. Room #207")
        room2_label.grid(row=4, column = 0)
        guest2_label = tk.Label(frame, text="Grace Gin")
        guest2_label.grid(row=5, column = 0)

        checkout_label = tk.Label(frame, text="Check-Out", bg='#C4C4C4')
        checkout_label.grid(row=1, column = 5)

        roomout1_label = tk.Label(frame, text="1. Room #128")
        roomout1_label.grid(row=2, column = 5)
        guestout1_label = tk.Label(frame, text="Peter Hat")
        guestout1_label.grid(row=3, column = 5)
        payment1_label = tk.Label(frame, text= "$ 480")
        payment1_label.grid(row=4, column = 5)

        roomout2_label = tk.Label(frame, text="2. Room #302")
        roomout2_label.grid(row=5, column = 5)
        guestout2_label = tk.Label(frame, text="Helen Gal")
        guestout2_label.grid(row=6, column = 5)
        payment2_label = tk.Label(frame, text="$ 600")
        payment2_label.grid(row=7, column = 5)

        total_label = tk.Label(frame, text="Total: $ 1080")
        total_label.grid(row=8, column = 6)
#frame.mainloop()
