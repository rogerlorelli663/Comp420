

class WindowStateManager:
    __current_window = None

    def __init__(self, initialWindow):
        self.open_window_screen(initialWindow)

    @staticmethod
    def open_window_screen(window):
        if WindowStateManager.__current_window is not None:
            WindowStateManager.__current_window.close()
        WindowStateManager.__current_window = window
