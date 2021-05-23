from Database import Database
from SessionStateManager import SessionStateManager


class UniGames:
    database = None

    def __init__(self):
        UniGames.database = Database("localhost", "root", "", "COMP420Project")
        session_manager = SessionStateManager()


if __name__ == '__main__':
    app = UniGames()
