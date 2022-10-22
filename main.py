from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class MainWindow(Screen):
    def up_peoples(self, x):
        peoples = int(self.peoples_lbl.text)
        peoples += x
        if peoples != 0:
            self.peoples_lbl.text = str(peoples)


class WindowManager(ScreenManager):
    pass


class FuelApp(MDApp):
    def build(self):
        kv = Builder.load_file("fuel.kv")
        return WindowManager()


if __name__ == '__main__':
  FuelApp().run()
