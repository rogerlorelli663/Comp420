from Customer import Customer
from MainScreen import MainScreen
from Unigames import UniGames
from Window import Window
from WindowStateManager import WindowStateManager


class LoginScreen(Window):
    def __init__(self):
        self.__display_login_window()
        self.is_enabled = True

    def __display_login_window(self):
        pass

    def __display_invalid_login_window(self):
        pass

    def __display_account_creation(self):
        pass

    def login(self):
        email = None
        password = None

        database = UniGames.database
        login = database.execute(f"call sign_in({email}, {password});")
        if login is not None and login:
            WindowStateManager.open_window_screen(MainScreen(Customer(login[0], login[3])))
        else:
            self.__display_invalid_login_window()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def close(self):
        pass
