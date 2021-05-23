from Commands.LoginCommand import LoginCommand
from Commands.CreateAccountCommand import CreateAccountCommand
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

        screens = [LoginScreen(self, name="login"), CreateAccountScreen(self, name="create")]
        for screen in screens:
            self.sm.add_widget(screen)
        self.sm.current = "login"

    def close(self):
        pass


class LoginScreen(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def __init__(self, window, **kw):
        super().__init__(**kw)
        self.window = window

    def login_button(self):
        if not LoginCommand(self.email.text, self.password.text).execute():
            InvalidAccount()

    def create_account_button(self):
        self.reset()
        self.window.sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        pass



class CreateAccountScreen(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    alias = ObjectProperty(None)

    def __init__(self, window, **kw):
        super().__init__(**kw)
        self.window = window


    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count(
                "@") == 1 and self.email.text.count(".") > 0:
            fullname = self.namee.text.split()
            if self.password != "" and len(fullname) > 1:
                CreateAccountCommand(fullname[0],fullname[1],self.alias.text,self.email.text,self.password.text).execute()

                AccountTaken()
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        self.window.sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""
        self.alias.text = ""

def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

def AccountTaken():
    pop = Popup(title='Account Already Exists',
                  content=Label(text='Please use a different email.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

def InvalidAccount():
    pop = Popup(title='Invalid Email/Password',
                content=Label(text='Password or email was invalid.'),
                size_hint=(None, None), size=(400, 400))

    pop.open()