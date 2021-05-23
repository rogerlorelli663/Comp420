from Commands.Command import Command


class RetrieveDlcGamesCommand(Command):
    def __init__(self, game_id):
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        sql = f'select dlc_id,dlc_title,DLC_PRICE,DLC_DISCOUNT,DLC_RELEASE_DATE from game_dlc where game_dlc.game_id = {self.game_id};'
        return database.execute(sql)
