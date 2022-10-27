from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from calculating import calculating
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.dialog import MDDialog


class MainWindow(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.settings = settings
        self.dialog = None

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

    def change_lang(self):
        import random
        self.sett_lang.secondary_text = random.choice(['Тык-тык', 'Ой-ой-ой'])

    def show_simple_dialog(self, inp: dict):
        it = inp["items"]
        items = []
        for item in it:
            items.append(OneLineIconListItem(text=item))
        self.dialog = MDDialog(title=inp["title"], type="simple", items=items)
        self.dialog.open()


class WindowManager(ScreenManager):
    pass


class FuelApp(MDApp):

    def build(self):
        Builder.load_file("fuel.kv")
        return WindowManager()


if __name__ == '__main__':
    settings = JsonStore("settings.json")
    FuelApp().run()
