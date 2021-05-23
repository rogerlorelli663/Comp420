from Commands.Command import Command


class LinkAccountCommand(Command):
    def __init__(self, cust_id, platform, alias):
        self.cust_id = cust_id
        self.platform = platform
        self.alias = alias
        
    def execute(self):
        from Unigames import UniGames
        from MainScreen import MainScreen
        database = UniGames.database
        database.execute(f"call link_account({self.cust_id}, {self.platform}, {self.alias});")
        # needs a procedure to get all aliases from customer
        if database.execute(f"call get_customer({self.cust_id});"):
            p_cust = MainScreen.personal_account.customer
            p_cust.steam_alias = ""
            p_cust.epic_alias = ""
            p_cust.uplay_alias = ""
            p_cust.gog_alias = ""
            p_cust.ea_alias = ""
