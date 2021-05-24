from Commands.RetrieveAccountCommand import RetrieveAccountCommand
from Window import Window, WindowManager
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label

personal_account = None

class MainWindow(Window):
    def __init__(self,customer):
        global personal_account
        personal_account = RetrieveAccountCommand(customer).execute()
        super().__init__()
        self.kivy = Builder.load_file("main.kv")

        screens = [MainScreen(self, name="main")]
        for screen in screens:
            self.sm.add_widget(screen)
        self.sm.current = "main"

    def close(self):
        pass

class MainScreen(Screen):
    alias = ObjectProperty(None)

    def __init__(self, window, **kw):
        super().__init__(**kw)
        self.window = window

    def on_enter(self, *args):
        global personal_account
        self.alias.text = "Alias: " + personal_account.customer.alias

    def display_personal_library(self):
        # shows list of owned games
        # basic display of game titles
        # on select -> display info of game on main screen
        # search criteria -> e.g. filter by category
        # shows list of friends
        # basic display of friend names
        # on select -> display info of freind
        pass

    def display_store_page(self):
        # shows list of all games
        # search criteria to filter for games
        # search criteria will obtain results from db
        # able to add, remove, edit games
        # game info in main window
        # add game to personal library
        pass

    def display_message_screen(self):
        # display friends and messages
        pass

    def close(self):
        pass
