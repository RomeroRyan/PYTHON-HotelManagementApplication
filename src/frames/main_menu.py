try:
    import ttk
except ImportError:
    try:
        import tkinter.ttk as ttk
    except ImportError:
        print("Could not import tkinter!")

from src.frames.frame import Frame
from src.frames.capability_1 import CapabilityOne
from src.frames.capability_2 import CapabilityTwo
from src.frames.capability_3 import CapabilityThree
from src.frames.capability_4 import CapabilityFour
from src.frames.capability_5 import CapabilityFive
from src.frames.capability_6 import CapabilitySix
from src.frames.capability_7 import CapabilitySeven
from src.frames.capability_8 import CapabilityEight

class MainFrame(Frame):
    def __init__(self, parent=None, title=None):
        super().__init__(parent, title)
        self.notebook = None
        self.add_notebook(pack_cfg={"pady": 15})

        capability_one_frame_config = {
            "text": "Room Status"
        }
        self.capability_one = CapabilityOne(
                        self.notebook,
                        frame_config=capability_one_frame_config
                    )
        self.add_tab(self.capability_one.get_frame(), capability_one_frame_config["text"])

        capability_two_frame_config = {
            "text": "Show Rooms"
        }
        self.capability_two = CapabilityTwo(
                        self.notebook,
                        frame_config=capability_two_frame_config
                    )
        self.add_tab(self.capability_two.get_frame(), capability_two_frame_config["text"])

        capability_three_frame_config = {
            "text": "Reservation"
        }
        self.capability_three = CapabilityThree(
                        self.notebook,
                        frame_config=capability_three_frame_config
                    )
        self.add_tab(self.capability_three.get_frame(), capability_three_frame_config["text"])

        capability_four_frame_config = {
            "text": "Housekeeping"
        }
        self.capability_four = CapabilityFour(
                        self.notebook,
                        frame_config=capability_four_frame_config
                    )
        self.add_tab(self.capability_four.get_frame(), capability_four_frame_config["text"])

        capability_five_frame_config = {
            "text": "Manage Guest"
        }
        self.capability_five = CapabilityFive(
                        self.notebook,
                        frame_config=capability_five_frame_config
                    )
        self.add_tab(self.capability_five.get_frame(), capability_five_frame_config["text"])

        capability_six_frame_config = {
            "text": "All Guest"
        }
        self.capability_six = CapabilitySix(
                        self.notebook,
                        frame_config=capability_six_frame_config
                    )
        self.add_tab(self.capability_six.get_frame(), capability_six_frame_config["text"])

        capability_seven_frame_config = {
            "text": "Search Guest"
        }
        self.capability_seven = CapabilitySeven(
                        self.notebook,
                        frame_config=capability_seven_frame_config
                    )
        self.add_tab(self.capability_seven.get_frame(), capability_seven_frame_config["text"])

        capability_eight_frame_config = {
            "text": "Report"
        }
        self.capability_eight = CapabilityEight(
                        self.notebook,
                        frame_config=capability_eight_frame_config
                    )
        self.add_tab(self.capability_eight.get_frame(), capability_eight_frame_config["text"])

    def add_notebook(self, pack_cfg={"packable": None, "pack_config": None}):
        self.notebook = ttk.Notebook(self.parent)
        packable = {"packable": self.notebook, "pack_config": pack_cfg}
        self.add_packable(packable)

    def add_tab(self, tab, text):
        self.notebook.add(tab, text=text)

    def render_frame(self, forget_frames=False):
        self.reset_packables()
        self.add_packable({"packable": self.notebook, "pack_cfg": {"expand": 1, "fill": "both"}})
        self.capability_one.add_button(self.notebook, pack_cfg={"text": "Hello", 'width': 30, 'height': 30})