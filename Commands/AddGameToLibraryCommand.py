from Commands.Command import Command


class AddGameToLibraryCommand(Command):
    def __init__(self, cust_id, game_id, plat_num, exe_dir):
        self.cust_id = cust_id
        self.game_id = game_id
        self.plat_num = plat_num
        self.exe_dir = exe_dir

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        # have add_game procedure return game
        game = database.execute(f"call add_game({self.cust_id}, {self.game_id}, {self.plat_num}, {self.exe_dir});")
        if game:
            # Add game to personal library
            return True
        else:
            return False
