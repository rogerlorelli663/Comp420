from Commands.Command import Command


class RetrieveStoreLinksCommand(Command):
    def init(self, game_id):
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        return database.execute(f"call get_store_links({self.game_id});")
