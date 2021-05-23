from Commands.Command import Command


class CreateDlcCommand(Command):
    def __init__(self, game_id, developer, price, discount, release_date):
        self.game_id = game_id
        self.developer = developer
        self.price = price
        self.discount = discount
        self.release_date = release_date

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        if database.execute(f"call new_dlc({self.game_id}, {self.developer}, {self.price}, {self.discount}, {self.release_date});"):
            return True
        else:
            return False