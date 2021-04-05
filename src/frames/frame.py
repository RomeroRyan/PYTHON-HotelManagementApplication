try:
    import Tkinter as tk
except ImportError:
    try:
        import tkinter as tk
    except ImportError:
        print("Could not import tkinter!")

class Frame:
    def __init__(self, parent, title_config=None, frame_config=None):
        self.title = None
        self.parent = parent
        self.frame = None

        self.packables = []

        if title_config is not None:
            self.set_title(title_config)

        if frame_config is not None:
            self.set_frame(parent, frame_config)

    def set_frame(self, parent, configuration, pack_cfg={}):
        self.frame = tk.LabelFrame(parent, cnf=configuration)
        packable = {"packable": self.frame, "pack_config": pack_cfg}
        self.add_packable(packable)

    def get_frame(self):
        return self.frame

    def set_title(self, config, pack_cfg={}):
        cnf = config or {"text": "Lorem Ipsum", "font": ("Times", 20, "bold")}
        self.title = tk.Label(self.parent, cnf=cnf)
        packable = {"packable": self.title, "pack_config": pack_cfg}
        self.add_packable(packable)
        
    def add_button(self, config, pack_cfg={}):
        cnf = config or {"text": "Lorem Ipsum", "font": ("Times", 20, "bold")}
        packable = {"packable": tk.Button(self.frame, cnf=cnf), "pack_config": pack_cfg}
        self.add_packable(packable)

    def add_packable(self, packable):
        self.packables.append(packable)

    def reset_packables(self):
        self.packables = []

    def render_frame(self, forget_frames=False):
        if forget_frames:
            self.forget_frame()
        for packable in self.packables:
            packable['packable'].pack(packable['pack_config'])
    def forget_frame(self):
        self.frame.forget()
