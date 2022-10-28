from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from calculating import calculating
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout


class LangDia(BoxLayout):
    pass


class MoneyDia(BoxLayout):
    pass


class MainWindow(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = settings

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
        self.result.text = f'{calculating(km, cons, prc, peoples)} {self.settings["money"]}'

    def change_sett(self, ident, key, val):
        pass

    @staticmethod
    def show_simple_dialog(cls: dict):
        if cls["cls"] == "lang":
            clas = LangDia
        else:
            clas = MoneyDia
        dialog = MDDialog(title=cls["title"], content_cls=clas(), type="custom")
        dialog.open()


class WindowManager(ScreenManager):
    pass


class FuelApp(MDApp):

    def build(self):
        return WindowManager()


if __name__ == '__main__':
    settings = JsonStore("settings.json")
    FuelApp().run()
