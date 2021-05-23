from Commands.RetrieveAccountCommand import RetrieveAccountCommand
from Window import Window


class MainWindow(Window):
    personal_account = None

    def __init__(self, customer):
        MainWindow.personal_account = RetrieveAccountCommand(customer)

    def display_personal_library(self):
        # shows list of owned games
            # basic display of game titles
            # on select -> display info of game on main screen
            # search criteria -> e.g. filter by category
        # shows list of friends
            # basic display of friend names
            # on select -> display info of freind
        pass

    def display_store_page(self):
        # shows list of all games
            # search criteria to filter for games
                # search criteria will obtain results from db
        # able to add, remove, edit games
            # game info in main window
        # add game to personal library
        pass

    def display_message_screen(self):
        # display friends and messages
        pass

    def close(self):
        pass
