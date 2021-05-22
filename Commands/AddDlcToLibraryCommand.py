from Commands.Command import Command


class AddDlcToLibraryCommand(Command):
    def __init__(self, cust_id, dlc_id):
        self.cust_id = cust_id
        self.dlc_id = dlc_id

    def execute(self):
        from Unigames import UniGames
        database = UniGames.database
        # Have add_dlc procedure return dlc
        dlc = database.execute(f"call add_dlc({self.cust_id}, {self.dlc_id});")
        if dlc:
            # Add dlc to personal game list
            return True
        else:
            return False
