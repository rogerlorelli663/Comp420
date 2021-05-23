from Commands.Command import Command


class LinkGamePlatformCommand(Command):
    def __init__(self, game_id, platform_num, url):
        self.game_id = game_id
        self.platform_num = platform_num
        self.url = url

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        if database.execute(f"call link_game_platform({self.game_id}, {self.platform_num}, {self.url});"):
            return True
        else:
            return False
