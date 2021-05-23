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
        sql = f'SELECT game_id,g_title from basicgamelistcollection join game_library_entry using (game_id) ' \
              f'join customer using (cust_id) where cust_id = {self.customer.ident}'
        d_library = database.execute(sql)
        sql = f'select friend_id, cust_alias, steam_alias, epic_alias, uplay_alias, gog_alias, ea_alias, F_SHARE_SETTING,F_REAL_NAME from AdvancedCustInfo ' \
              f'join friend on friend.friend_id = AdvancedCustInfo.cust_id where friend.cust_id = id;'
        d_friends = database.execute(sql)
        library = []
        friends = []
        if d_library is not None:
            for d_game in d_library:
                library.append(Game(d_game[0], d_game[1]))
        if d_friends is not None:
            for d_friend in d_friends:
                friends.append(Customer(d_friend[0], d_friend[1]))
        return Account(self.customer, library, friends)
