from src.frames.frame import Frame

class CapabilitySix(Frame):
    def __init__(self, parent=None, title_config=None, frame_config=None):
        super().__init__(parent, title_config=title_config, frame_config=frame_config)
        self.add_packable({"packable": self.get_frame(), "pack_config": {"fill": "both", "expand": 1}})