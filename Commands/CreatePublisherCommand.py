from Commands.Command import Command


class CreatePublisherCommand(Command):
    def __init__(self, company, phone, email, url):
        self.company = company
        self.phone = phone
        self.email = email
        self.url = url

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        if database.execute(f"call create_publisher({self.company}, {self.phone}, {self.email}, {self.url});"):
            return True
        else:
            return False
