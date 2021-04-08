from src.frames.frame import Frame

class CapabilityTwo(Frame):
    def __init__(self, parent=None, title_config=None, frame_config=None):
        super().__init__(parent, title_config=title_config, frame_config=frame_config)

    def add_button(self):
        super().add_button(super().frame, pack_cfg={"text": "Hello", 'width': 30, 'height': 30})