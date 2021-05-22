from Account import Account
from Customer import Customer
from Game import Game
from Unigames import UniGames


class MainScreen:
    personal_account = None

    def __init__(self, customer):
        database = UniGames.database
        d_library = database.execute(f"retrievegamelibrary({customer.CUST_ID});")
        d_friends = database.execute(f"get_friends_list({customer.CUST_ID})")
        library = []
        friends = []
        if d_library is not None:
            for d_game in d_library:
                library.append(Game(d_game[0], d_game[1]))
        if d_friends is not None:
            for d_friend in d_friends:
                friends.append(Customer(d_friend[0], d_friend[1]))
        MainScreen.personal_account = Account(customer, library, friends)

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
