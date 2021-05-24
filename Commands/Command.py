from Unigames import UniGames
from Game import Game
from Account import Account
from Customer import Customer
class Command:
    def execute(self):
        pass


class AddDlcToLibraryCommand(Command):
    def __init__(self, cust_id, dlc_id):
        self.cust_id = cust_id
        self.dlc_id = dlc_id

    def execute(self):
        database = UniGames.database
        # Have add_dlc procedure return dlc
        dlc = database.execute_commit(f"call add_dlc({self.cust_id}, {self.dlc_id});")
        if dlc:
            # Add dlc to personal game list
            return True
        else:
            return False


class AddGameToLibraryCommand(Command):
    def __init__(self, cust_id, game_id, plat_num, exe_dir):
        self.cust_id = cust_id
        self.game_id = game_id
        self.plat_num = plat_num
        self.exe_dir = exe_dir

    def execute(self):
        database = UniGames.database
        # have add_game procedure return game
        game = database.execute_commit(f"call add_game({self.cust_id}, {self.game_id}, {self.plat_num}, \'{self.exe_dir}\');")
        if game:
            # Add game to personal library
            return True
        else:
            return False


class CreateAccountCommand(Command):
    def __init__(self, fname, lname, alias, email, password):
        self.fname = fname
        self.lname = lname
        self.alias = alias
        self.email = email
        self.password = password

    def execute(self):
        database = UniGames.database
        database.execute_commit(f"call create_cust_account(\'{self.fname}\', \'{self.lname}\', \'{self.alias}\', \'{self.email}\', \'{self.password}\');")



class CreateDeveloperCommand(Command):
    def __init__(self, company, phone, email, url):
        self.company = company
        self.phone = phone
        self.email = email
        self.url = url

    def execute(self):
        database = UniGames.database
        if database.execute_commit(f"call create_developer({self.company}, {self.phone}, {self.email}, {self.url});"):
            return True
        else:
            return False


class CreateDlcCommand(Command):
    def __init__(self, game_id, developer, price, discount, release_date):
        self.game_id = game_id
        self.developer = developer
        self.price = price
        self.discount = discount
        self.release_date = release_date

    def execute(self):
        database = UniGames.database
        if database.execute_commit(f"call new_dlc({self.game_id}, {self.developer}, {self.price}, {self.discount}, {self.release_date});"):
            return True
        else:
            return False


class CreateMessageCommand(Command):
    def init(self, cust_id, message, image_path):
        self.cust_id = cust_id
        self.message = message
        self.image_path = image_path

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        sql_command = f'insert into message values(null, now(), ' \
                      f'{self.message}, {self.image_path}, {self.cust_id}); select message_id from message where m_create_date = date_now ' \
                      f'and m_created_by = cus_id; '
        return database.execute_commit(sql_command)


class CreateNewGame(Command):
    def __init__(self, title, publisher, developer, esrb, price, discount, release_date, max_spec, min_spec):
        self.title = title
        self.publisher = publisher
        self.developer = developer
        self.esrb = esrb
        self.price = price
        self.discount = discount
        self.release_date = release_date
        self.max_spec = max_spec
        self.min_spec = min_spec

    def execute(self):
        database = UniGames.database
        if database.execute_commit(f"call new_game({self.title}, {self.publisher}, {self.developer}, {self.esrb}, {self.price}, {self.discount}, {self.release_date}, {self.max_spec}, {self.min_spec});"):
            return True
        else:
            return False


class CreatePublisherCommand(Command):
    def __init__(self, company, phone, email, url):
        self.company = company
        self.phone = phone
        self.email = email
        self.url = url

    def execute(self):
        database = UniGames.database
        if database.execute_commit(f"call create_publisher({self.company}, {self.phone}, {self.email}, {self.url});"):
            return True
        else:
            return False


class LinkAccountCommand(Command):
    def __init__(self, cust_id, platform, alias):
        self.cust_id = cust_id
        self.platform = platform
        self.alias = alias

    def execute(self):
        database = UniGames.database
        database.execute_commit(f"call link_account({self.cust_id}, {self.platform}, {self.alias});")
        # needs a procedure to get all aliases from customer


class LinkGamePlatformCommand(Command):
    def __init__(self, game_id, platform_num, url):
        self.game_id = game_id
        self.platform_num = platform_num
        self.url = url

    def execute(self):
        database = UniGames.database
        if database.execute_commit(f"call link_game_platform({self.game_id}, {self.platform_num}, {self.url});"):
            return True
        else:
            return False


class LoginCommand(Command):
    def __init__(self, email, password):
        self.__email = email
        self.__password = password

    def execute(self):
        database = UniGames.database
        sql = f'select * from customer where cust_email = \"{self.__email}\" and pass = \"{self.__password}\";'
        login = database.execute(sql)
        return login


class RetrieveAccountCommand(Command):
    def __init__(self, customer):
        self.customer = customer

    def execute(self):
        database = UniGames.database
        sql = f'SELECT game_id, g_title, g_esrb, g_price, g_avg_rating from game join game_library_entry using (game_id) ' \
              f'join customer using (cust_id) where cust_id = {self.customer.ident}'
        d_library = database.execute(sql)
        sql = f'select friend_id, cust_alias, steam_alias, epic_alias, uplay_alias, gog_alias, ea_alias, F_SHARE_SETTING,F_REAL_NAME from AdvancedCustInfo ' \
              f'join friend on friend.friend_id = AdvancedCustInfo.cust_id where friend.cust_id = {self.customer.ident};'
        d_friends = database.execute(sql)
        library = []
        friends = []
        if d_library is not None:
            for d_game in d_library:
                library.append(Game(d_game[0], d_game[1],d_game[2], d_game[3], d_game[4]))
        if d_friends is not None:
            for d_friend in d_friends:
                customer = Customer(d_friend[0], d_friend[1], d_friend[2], d_friend[3], d_friend[4], d_friend[5], d_friend[6]," ", " ")
                friends.append(customer)
        return Account(self.customer, library, friends)


class RetrieveDlcGamesCommand(Command):
    def __init__(self, game_id):
        self.game_id = game_id

    def execute(self):
        database = UniGames.database
        return database.execute(f"call get_completed_dlc_list({self.game_id});")


class RetrieveLibraryDlcGameCommand(Command):
    def __init__(self, cust_id, game_id):
        self.cust_id = cust_id
        self.game_id = game_id

    def execute(self):
        database = UniGames.database
        return database.execute(f"call get_dlc_library({self.cust_id}, {self.game_id});")


class CreateMessageCommand(Command):
    def init(self, recipient_id):
        self.recipient_id = recipient_id

    def execute(self):
        database = UniGames.database
        sql_command = f'SELECT m_content, m_image_path, m_created_by, m_create_date from message join recipient using (message_id)  where recipient.cust_id = {self.recipient_id} and r_read = 0; update recipient set r_read = 1 where cust_id = {self.recipient_id} and r_read = 0;'
        return database.execute_commit(sql_command)


class RetrieveStoreLinksCommand(Command):
    def init(self, game_id):
        self.game_id = game_id

    def execute(self):
        database = UniGames.database
        return database.execute(f"call get_store_links({self.game_id});")


class SendMessageCommand(Command):
    def init(self, message_id, recipient):
        self.message_id = message_id
        self.recipient = recipient

    def execute(self):
        database = UniGames.database
        database.execute_commit(f"call send_message({self.message_id}, {self.recipient})")


class CreateCollectionCommand(Command):
    def __init__(self, cust_id, name):
        self.cust_id = cust_id
        self.name = name

    def execute(self):
        database = UniGames.database
        database.execute_commit(f"call create_collection({self.cust_id}, {self.name})")


class AddCollectionEntryCommand(Command):
    def __init__(self, game_id, collection_id):
        self.game_id = game_id
        self.collection_id = collection_id

    def execute(self):
        database = UniGames.database
        database.execute_commit(f"call add_collection_entry({self.game_id}, {self.collection_id})")


class RetrieveCollectionCommand(Command):
    def __init__(self, cust_id, collection_name):
        self.cust_id = cust_id
        self.collection_name = collection_name

    def execute(self):
        database = UniGames.database
        sql_command = f'select g_title from game join collection_entry using (game_id) join customer_collection using (collection_id) where c_name = {self.collection_name} and customer_collection.cust_id = {self.cust_id};'
        return database.execute(sql_command)


class CreateReviewCommand(Command):
    def __init__(self, cust_id, game_id, rating, message):
        self.cust_id = cust_id
        self.game_id = game_id
        self.rating = rating
        self.message = message

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        database.execute_commit(f"call create_review({self.cust_id}, {self.game_id}, {self.rating}, {self.message})")


class AddFriendCommand(Command):
    def __init__(self, cust_id, friend_id):
        self.cust_id = cust_id
        self.friend_id = friend_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        database.execute_commit(f"call add_friend({self.cust_id}, {self.friend_id})")


class UpdateFriendShare(Command):
    def __init__(self, cust_id, friend_id, setting):
        self.cust_id = cust_id
        self.friend_id = friend_id
        self.setting = setting

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        database.execute(f"call update_friend_share({self.cust_id}, {self.friend_id}, \'{self.setting})\'")


class UpdateFriendRn(Command):
    def __init__(self, cust_id, friend_id, real_name):
        self.cust_id =cust_id
        self.friend_id = friend_id
        self.real_name = real_name

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        database.execute(f"call update_friend_rn({self.cust_id}, {self.friend_id}, {self.real_name})")











