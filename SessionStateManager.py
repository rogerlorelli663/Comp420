

class SessionStateManager:
    __current_window = None

    def __init__(self):
        from LoginWindow import LoginWindow
        self.open_window_screen(LoginWindow())

    @staticmethod
    def open_window_screen(window):
        if SessionStateManager.__current_window is not None:
            SessionStateManager.__current_window.close()
        SessionStateManager.__current_window = window
        window.run()
