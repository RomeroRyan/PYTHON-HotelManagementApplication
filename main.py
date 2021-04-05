from src.app import App

if __name__ == "__main__":
    ROOT_TITLE = "Hotel Management App"
    ROOT_DIMENSIONS = "600x400"
    app = App()
    app.setup(ROOT_TITLE, ROOT_DIMENSIONS)
    app.run()
