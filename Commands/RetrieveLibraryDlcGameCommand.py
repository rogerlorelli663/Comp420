from Commands.Command import Command


class RetrieveLibraryDlcGameCommand(Command):
    def __init__(self, cust_id, game_id):
        self.cust_id = cust_id
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        sql = f'select dlc_title,DLC_RELEASE_DATE from game_dlc join dlc_library_entry using (dlc_id) where dlc_library_entry.cust_id = {self.cust_id} and game_dlc.game_id = {self.game_id};'
        return database.execute(sql)
