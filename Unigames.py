from Database import Database
from Commands.Command import *
import os

platforms =  ['STEAM','UPLAY','GOG','EA','EPIC']

class UniGames:
    database = Database("localhost", "manager123", "password", "COMP420Project")
    account = None
    def __init__(self):
        value = None
        while value != 0:
            print("Please choose from the following options: [0-2]")
            value = int(input(f'1. Sign In\n'
                              f'2. Create New Account\n'
                              f'0. Exit\n'))
            if value == 1:
                self.Login()
                self.MainScreen()
            elif value == 2:
                self.NewAccount()
                self.MainScreen()


    def Login(self):
        os.system('cls')
        print('Login Screen:\n')
        while True:
            email = input("Email: ")
            password = input("Password: ")
            result = LoginCommand(email,password).execute()
            if result is not None and len(result) > 0:
                customer = Customer(result[0][0],result[0][3],result[0][4],result[0][5],result[0][6],result[0][7],result[0][8],result[0][1],result[0][2])
                self.account = RetrieveAccountCommand(customer).execute()
                break
            else:
                print('Invalid information\n')

    def NewAccount(self):
            os.system('cls')
            print("Enter the following information:\n")
            fname = input("First Name: ")
            lname = input("Last Name: ")
            alias = input("Alias: ")
            email = input("Email: ")
            password = input("Password: ")
            CreateAccountCommand(fname, lname, alias, email, password).execute()
            self.Login()

    def MainScreen(self):
        os.system('cls')
        print(f'Alias: {self.account.customer.alias}\n')
        value = None
        while value != 0:
            print("Please choose from the following options: [0-2]")
            value = int(input(f'1. View Friends Screen\n'
                              f'2. View Library Screen\n'
                              f'3. Search for a game\n'
                              f'0. Back'))

            if value == 1:
                self.Friends()
            elif value == 2:
                self.Library()

    def Library(self):
        os.system('cls')
        print(f'Library:\n')
        value = None
        while value != 0:
            print("Please choose from the following options: [0-2]")
            value = int(input(f'1. View Library\n'
                              f'2. View Collections\n'
                              f'0. Back\n'))
            if value == 1:
                self.DisplayLibrary()
                print("Please choose from the following options: [0-2]")
                value = int(input(f'1. Add Game\n'
                                  f'0. Back\n'))
                if value == 1:
                    self.AddGame()
            elif value == 3:
                self.AddGame()
            elif value == 4:
                self.ReviewGame()

    def SelectGame(self, game_code):
        print(f'ID\tTitle\tCode\tESRB\tRating\tPath\n')
        print(f'{self.account.owned_games[game_code].ident}  {self.account.owned_games[game_code].title}: {self.account.owned_games[game_code].ident} {self.account.owned_games[game_code].esrb}  {self.account.owned_games[game_code].avg_rating} {self.account.owned_games[game_code].path}\n')
        choice = input('\nReview Game: Y/N?')
        if choice != "N":
            self.ReviewGame(game_code)


    def DisplayLibrary(self):
        choice = None
        while choice != -1:
            games = self.account.owned_games
            i = 1
            print('Games Library:\n')
            for game in games:
                print(f'#{i} {game.title}: {game.esrb}  {game.avg_rating}\n')
                i = i + 1
            choice = int(input("Select Game: 0 to go back"))
            choice = choice - 1
            if choice != -1:
                self.SelectGame(choice)



    def ReviewGame(self,game_code):
        os.system('cls')
        print(f'Review: {self.account.owned_games[game_code].title}\n')
        message = input("Message: ")
        rating = int(input("Score (0-10): "))
        CreateReviewCommand(self.account.customer.ident,self.account.owned_games[game_code].ident,rating,message).execute()




    def AddGame(self):
        game = int(input("Enter Game Code: "))
        path = input("Executable Path: ")
        print("Platform Number: \n")
        for i in range(0,len(platforms)):
            print(f'{i + 1}: {platforms[i]}')
        plat = int(input('\n'))
        AddGameToLibraryCommand(self.account.customer.ident, game,plat,path).execute()
        self.account = RetrieveAccountCommand(self.account.customer).execute()
        value = input('Add DLC: Y/N?')
        while value != 'N':
            self.AddDLC(game)

    def AddDLC(self,game_code):
        dlcs = RetrieveDlcGamesCommand(game_code).execute()
        if len(dlcs) > 0:
            for dlc in dlcs:
                print(dlc + '\n')
            dlc_code = int(input("DLC Code:"))
            AddDlcToLibraryCommand(self.account.customer.ident, dlc_code).execute()
        else:
            print("No DLC for this title\n")

    def Friends(self):
        os.system('cls')
        print(f'Friends:\n')
        value = None
        while value != 0:
            print("Please choose from the following options: [0-2]")
            value = int(input(f'1. View Friends\n'
                              f'2. Add Friend\n'
                              f'0. Back\n'))
            if value == 1:
                friends = self.account.friends
                i = 1
                print("#\tAlias:\tSteam:\tEpic\tUplay\tGOG\tEA\n")
                for friend in friends:
                    print(f'{i}\t{friend.alias}\t{friend.steam_alias}\t{friend.epic_alias}\t{friend.uplay_alias}\t{friend.gog_alias}\t{friend.ea_alias}\n')
                    i = i + 1
            elif value == 2:
                self.AddFriend()


    def AddFriend(self):
        value = int(input("Enter Friend Code: "))
        AddFriendCommand(self.account.customer.ident,value).execute()
        self.account = RetrieveAccountCommand(self.account.customer).execute()



if __name__ == '__main__':
    app = UniGames()
