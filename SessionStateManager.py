

class SessionStateManager:
    __current_window = None

    def __init__(self):
        from LoginScreen import LoginScreen
        self.open_window_screen(LoginScreen())

    @staticmethod
    def open_window_screen(window):
        if SessionStateManager.__current_window is not None:
            SessionStateManager.__current_window.close()
        SessionStateManager.__current_window = window
