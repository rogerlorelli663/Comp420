from Commands.Command import Command
from Customer import Customer
from MainScreen import MainScreen
from Unigames import UniGames
from SessionStateManager import SessionStateManager


class LoginCommand(Command):
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def execute(self):
        database = UniGames.database
        login = database.execute(f"call sign_in({self.__email}, {self.__password});")
        if login is not None and login:
            SessionStateManager.open_window_screen(MainScreen(Customer(login[0], login[3])))
            return True
        else:
            return False
