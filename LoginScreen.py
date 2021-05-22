from Commands.LoginCommand import LoginCommand
from Window import Window


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
        email = ""
        password = ""
        isLoggedIn = LoginCommand(email, password)

    def close(self):
        pass
