# Hotel Assignment Project
#
import json
from guest import Guest
from guest_manager import *
try:
    import Tkinter as tk
    import ttk
except ImportError:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")


def main():
    from capabilities.capability_one import CapabilityOne
    from capabilities.capability_two import CapabilityTwo
    from capabilities.capability_three import CapabilityThree
    from capabilities.capability_four import CapabilityFour
    from capabilities.capability_five import CapabilityFive
    from capabilities.capability_six import CapabilitySix
    from capabilities.capability_seven import CapabilitySeven
    from capabilities.capability_eight import CapabilityEight

    from guest import Guest

    # Load room data

    # List of all rooms (initialize every room in the hotel)

    # ============================================================================================
    # SET DEFAULTS FOR THE MAIN WINDOWS
    '''
        This code is what influences the main window that pops up as soon as the app runs.
        (size of window, name of window, etc)
        root "hosts" all the frames (screens) that are being displayed in the GUI
    '''
    root = tk.Tk()
    root.title("Hotel Management App")
    root.geometry("1920x1080")
    # ============================================================================================
    # CREATE FRAMES
    '''
        This code initializes the frames(screens) that we will be using.
        WelcomeFrame is the first screen and serves no purpose other then to welcome users.
        WelcomeFrame leads to main_frame, which hosts the tab system (my_tabs).
        my_tabs hosts all our frames, allowing our frames to be swapped and displayed.
            (so our capability screens are in a tab widget which is displayed on the main_frame)
            (a group of frames within a single frame)
    '''
    welcome_frame = tk.LabelFrame(root, padx=5, pady=5)
    main_frame = tk.Frame(root)

    # create tab widget before creating capability frames
    my_tabs = ttk.Notebook(main_frame)
    my_tabs.pack(pady=15)

    # create capability frames
    frame1 = tk.Frame(my_tabs)  # capability 1
    frame2 = tk.Frame(my_tabs)  # capability 2
    frame3 = tk.Frame(my_tabs)  # capability 3
    frame4 = tk.Frame(my_tabs)  # capability 4
    frame5 = tk.Frame(my_tabs)  # capability 5
    frame6 = tk.Frame(my_tabs)  # capability 6
    frame7 = tk.Frame(my_tabs)  # capability 7
    frame8 = tk.Frame(my_tabs)  # capability 8

    # ============================================================================================
    # WELCOME: CODE BLOCK

    def go_menu():
        welcome_frame.forget()
        main_frame.pack()

    # WELCOME: create widgets
    welcome_title = tk.Label(
        welcome_frame, text="Hotel Management App", font=("Times", 30, "bold"))
    welcome_button = tk.Button(
        welcome_frame, text="Start", padx=25, command=go_menu)

    # WELCOME: set widgets
    welcome_title.pack()
    welcome_button.pack()
    welcome_frame.pack(pady=125)

    # ============================================================================================
    # MAIN: CODE BLOCK

    # MAIN: create widgets
    quit_label = tk.Button(main_frame, text="Quit", font=(
        "Times", 20, "bold"), command=root.quit)

    # MENU: set widgets
    quit_label.pack()
    # ============================================================================================

    # CALL CODE INITIALIZER HERE
    guests = get_guests()
    capability_one = CapabilityOne(frame1, my_tabs, frame6)
    capability_two = CapabilityTwo(frame2)
    capability_three = CapabilityThree(frame3, my_tabs, frame5)
    capability_four = CapabilityFour(frame4)
    capability_five = CapabilityFive(frame5, guests[0].get_id())
    capability_six = CapabilitySix(frame6)
    capability_seven = CapabilitySeven(frame7)
    capability_eight = CapabilityEight(frame8)

    # ============================================================================================
    # SET CAPABILITY FRAMES AND ADDS THEM INTO TAB SYSTEM
    '''
        "Setting(pack)" can be seen as "finalizing a screen".
        Once you have define and added all the desired widgets you
        want on a screen, you pack it, meaning it done being
        changed and can now be visible on screen
    '''
    # packs the frames
    frame1.pack(fill="both", expand=1)
    frame2.pack(fill="both", expand=1)
    frame3.pack(fill="both", expand=1)
    frame4.pack(fill="both", expand=1)
    frame5.pack(fill="both", expand=1)
    frame6.pack(fill="both", expand=1)
    frame7.pack(fill="both", expand=1)
    frame8.pack(fill="both", expand=1)

    # adds frames to tab system
    my_tabs.add(frame1, text="Room Status")
    my_tabs.add(frame2, text="Show Rooms")
    my_tabs.add(frame3, text="Reservation")
    my_tabs.add(frame4, text="Housekeeping")
    my_tabs.add(frame5, text="Guest Profile")
    my_tabs.add(frame6, text="All Guest")
    my_tabs.add(frame7, text="Guest search")
    my_tabs.add(frame8, text="Report")

    # ============================================================================================
    # Ending of GUI CODE
    root.mainloop()


if __name__ == "__main__":
    main()
