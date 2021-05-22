from Account import Account
from Commands.Command import Command
from Customer import Customer
from Game import Game
from Unigames import UniGames


class RetrieveAccountCommand(Command):
    def __init__(self, customer):
        self.customer = customer

    def execute(self):
        database = UniGames.database
        d_library = database.execute(f"call retrievegamelibrary({self.customer.ident});")
        d_friends = database.execute(f"call get_friends_list({self.customer.ident});")
        library = []
        friends = []
        if d_library is not None:
            for d_game in d_library:
                library.append(Game(d_game[0], d_game[1]))
        if d_friends is not None:
            for d_friend in d_friends:
                friends.append(Customer(d_friend[0], d_friend[1]))
        return Account(self.customer, library, friends)
