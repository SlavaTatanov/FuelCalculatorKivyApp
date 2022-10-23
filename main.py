from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from calculating import calculating
import settings


class MainWindow(Screen):
    def up_peoples(self, x):
        peoples = int(self.peoples_lbl.text)
        peoples += x
        if peoples != 0:
            self.peoples_lbl.text = str(peoples)

    def calculating(self):
        km = self.km.text
        cons = self.consumption.text
        prc = self.price.text
        peoples = self.peoples_lbl.text
        self.result.text = f'{calculating(km, cons, prc, peoples)} {settings.settings["currency"]}'


class WindowManager(ScreenManager):
    pass


class FuelApp(MDApp):
    def build(self):
        Builder.load_file("fuel.kv")
        settings.settings['currency'] = settings.sql_request_settings('currency')[0]
        return WindowManager()


if __name__ == '__main__':
    FuelApp().run()
