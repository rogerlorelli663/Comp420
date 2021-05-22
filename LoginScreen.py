from MainScreen import MainScreen
from Unigames import UniGames


class LoginScreen:
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
        login = database.execute(f"sign_in({email}, {password});")
        if login is not None and login:
            UniGames.open_window_screen(MainScreen(login[0]))
        else:
            self.__display_invalid_login_window()
