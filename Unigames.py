from Database import Database
from Commands.Command import *
import os

platforms =  ['STEAM','UPLAY','GOG','EA','EPIC']

class UniGames:
    database = Database("localhost", "root", "xSAp2]!(9#iu", "COMP420Project")
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
                              f'3. Add Game\n'
                              f'0. Back\n'))
            if value == 1:
                games = self.account.owned_games
                i = 1
                print('Games Library:\n')
                for game in games:
                    print(f'#{i}   {game.title}: {game.esrb}  {game.avg_rating}\n')
                    i = i + 1
            elif value == 3:
                self.AddGame()

    def AddGame(self):
        value = int(input("Enter Game Code: "))
        path = input("Executable Path: ")
        print("Platform Number: \n")
        for i in range(0,len(platforms)):
            print(f'{i + 1}: {platforms[i]}')
        plat = int(input('\n'))
        AddGameToLibraryCommand(self.account.customer.ident, value,plat,path).execute()
        self.account = RetrieveAccountCommand(self.account.customer).execute()

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
