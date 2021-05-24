from kivy.app import App
from kivy.uix.screenmanager import ScreenManager


class WindowManager(ScreenManager):
    pass


class Window(App):
    kivy = None
    #sm = WindowManager()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sm = WindowManager()

    def build(self):
        return self.sm

    def close(self):
        Window.close()
