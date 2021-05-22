from Commands.Command import Command


class RetrieveLibraryDlcGameCommand(Command):
    def __init__(self, cust_id, game_id):
        self.cust_id = cust_id
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        return database.execute(f"call get_dlc_library({self.cust_id}, {self.game_id});")
