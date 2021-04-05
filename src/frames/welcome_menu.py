from src.frames.frame import Frame

class WelcomeFrame(Frame):
    def __init__(self, parent=None, title=None, title_config=None, frame_config=None, main_frame=None):
        super().__init__(parent, title_config, frame_config)
        self.main_frame = main_frame

    def switch_frames(self):
        super().get_frame().forget()
        super().reset_packables()
        for packable in self.main_frame.packables:
            super().add_packable(packable)
            
        super().render_frame(forget_frames=True)