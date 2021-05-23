from Commands.Command import Command


class RetrieveStoreLinksCommand(Command):
    def init(self, game_id):
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        sql = f'select plat_name, plat_website from game join game_platform using(game_id) where game.game_id = {self.game_id};'
        return database.execute(sql)
