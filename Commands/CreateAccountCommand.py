from Commands.Command import Command


class CreateAccountCommand(Command):
    def __init__(self, fname, lname, alias, email, password):
        self.fname = fname
        self.lname = lname
        self.alias = alias
        self.email = email
        self.password = password

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        if database.execute(f"call create_cust_account({self.fname}, {self.lname}, {self.alias}, {self.email}, {self.password});"):
            return True
        else:
            return False
