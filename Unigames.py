from Database import Database
from LoginScreen import LoginScreen
from WindowStateManager import WindowStateManager


class UniGames:
    database = None

    def __init__(self):
        UniGames.database = Database("", "", "", "")
        window_manager = WindowStateManager(LoginScreen())

if __name__ == '__main__':
    app = UniGames()
