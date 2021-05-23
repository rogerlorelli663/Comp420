from Commands.Command import Command


class CreateNewGame(Command):
    def __init__(self, title, publisher, developer, esrb, price, discount, release_date, max_spec, min_spec):
        self.title = title
        self.publisher = publisher
        self.developer = developer
        self.esrb = esrb
        self.price = price
        self.discount = discount
        self.release_date = release_date
        self.max_spec = max_spec
        self.min_spec = min_spec

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        if database.execute(f"call new_game({self.title}, {self.publisher}, {self.developer}, {self.esrb}, {self.price}, {self.discount}, {self.release_date}, {self.max_spec}, {self.min_spec});"):
            return True
        else:
            return False