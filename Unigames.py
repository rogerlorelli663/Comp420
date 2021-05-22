from Database import Database
from SessionStateManager import SessionStateManager


class UniGames:
    database = None

    def __init__(self):
        UniGames.database = Database("", "", "", "")
        session_manager = SessionStateManager()


if __name__ == '__main__':
    app = UniGames()
