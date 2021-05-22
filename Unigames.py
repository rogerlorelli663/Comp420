from Database import Database
from LoginScreen import LoginScreen


class UniGames:
    database = None
    __current_window = None

    def __init__(self):
        UniGames.database = Database("", "", "", "")
        self.open_window_screen(LoginScreen())

    @staticmethod
    def open_window_screen(window):
        __current_window = window


if __name__ is '__main__':
    app = UniGames()
