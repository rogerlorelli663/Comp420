from Commands.Command import Command
from Customer import Customer
from MainWindow import MainWindow
from Unigames import UniGames
from SessionStateManager import SessionStateManager


class LoginCommand(Command):
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def execute(self):
        database = UniGames.database
        sql = f'select * from customer where cust_email = \"{self.__email}\" and pass = \"{self.__password}\";'
        login = database.execute(sql)

        if login is not None and login:
            main = None
            SessionStateManager.open_window_screen(main=MainWindow())
            main.load_account(Customer(login[0][0], login[0][3], login[0][1], login[0][2], login[0][4],login[0][5],login[0][6],login[0][7],login[0][8]))
            return True
        else:
            return False
