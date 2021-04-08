# Hotel Assignment Project
#

try:
    import Tkinter as tk
    import ttk
except ImportError:
    try:
        import tkinter as tk
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")

# ============================================================================================
# CLASSES
# classes we may use when creating functionality to code (they do nothing atm)
import src.data.hotel_room
import src.data.guest

from src.frames.main_menu import MainFrame
from src.frames.welcome_menu import WelcomeFrame

# ============================================================================================
# SET DEFAULTS FOR THE MAIN WINDOWS

'''
    This code is what influences the main window that pops up as soon as the app runs.
    (size of window, name of window, etc)
    root "hosts" all the frames (screens) that are being displayed in the GUI
'''

class App:

    def __init__(self):
        self.root = None
        self.main_menu = None
        self.welcome_screen = None

    def create_root(self, root_title, root_dimensions):
        root = tk.Tk()
        root.title(root_title)
        root.geometry(root_dimensions)
        return root

    def create_main_menu(self, parent):
        main_frame = MainFrame(parent)

        main_frame_button_config = {
            "text": "Main Menu",
            "font": ("Times", 20, "bold")
        }
        main_frame.add_button(main_frame.frame, main_frame_button_config)
        return main_frame

    def create_welcome_screen(self, parent, main_menu):

        welcome_frame_config = { "text": "Totally Legit Hotel App"}
        welcome_frame = WelcomeFrame(
                        parent=parent,
                        frame_config=welcome_frame_config,
                        main_frame=main_menu)

        welcome_button_config = {
            "text": "Start",
            "padx": 25,
            "pady": 0,
            "command": welcome_frame.switch_frames
        }

        welcome_frame.add_button(welcome_frame.frame, welcome_button_config)
        welcome_frame.render_frame()

    def setup(self, title, dimensions):
        self.root = self.create_root(title, dimensions)
        self.main_menu = self.create_main_menu(self.root)
        self.welcome_screen = self.create_welcome_screen(self.root, self.main_menu)

    def run(self):
        self.root.mainloop()
