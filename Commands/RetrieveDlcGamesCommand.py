from Commands.Command import Command


class RetrieveDlcGamesCommand(Command):
    def __init__(self, game_id):
        self.game_id = game_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        return database.execute(f"call get_completed_dlc_list({self.game_id});")
