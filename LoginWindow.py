from Commands.LoginCommand import LoginCommand
from Window import Window, WindowManager

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class LoginWindow(Window):
    def __init__(self):
        super().__init__()
        self.kivy = Builder.load_file("login.kv")

        screens = [LoginScreen(name="login"), CreateAccountScreen(name="create")]
        for screen in screens:
            self.sm.add_widget(screen)
        self.sm.current = "login"

    def close(self):
        pass


class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_button(self):
        if not LoginCommand(self.email.text, self.password.text):
            pass

    def create_button(self):
        self.reset()

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        pass


class CreateAccountScreen(Screen):
    pass
