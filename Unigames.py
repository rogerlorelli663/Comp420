from Database import Database
from SessionStateManager import SessionStateManager


class UniGames:
    database = Database("localhost", "root", "xSAp2]!(9#iu", "COMP420Project")

    def __init__(self):
        session_manager = SessionStateManager()


if __name__ == '__main__':
    app = UniGames()
