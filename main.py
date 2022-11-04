from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from calculating import calculating, names
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.label import MDIcon, MDLabel
import appdata


class LangDia(BoxLayout):
    pass


class MoneyDia(BoxLayout):
    @staticmethod
    def upd(date):
        """
        changing secondary text label on settings screen
        """
        refs['MainWindow'].set_money.secondary_text = date  # in kv file


class MainWindow(Screen):

    def __new__(cls, *args, **kwargs):
        ref = super().__new__(cls)
        refs["MainWindow"] = ref
        return ref

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.save_button = False

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
        res = calculating(km, cons, prc, peoples, money["for_user"])
        if res != names['err']:
            self.result.text = f'{res.message}'
            if not self.save_button:
                self.save_button = True
                self.save.clear_widgets()
                self.save.add_widget(MDFillRoundFlatIconButton(text="Сохранить",
                                                               pos_hint={"center_x": .5, "center_y": .5},
                                                               icon="content-save-edit-outline",
                                                               on_press=lambda slf: self.save_result()))

        else:
            self.result.text = f'{res}'

    def save_result(self):
        self.save.clear_widgets()
        self.save.add_widget(MDIcon(icon="check-bold",
                                    pos_hint={"center_x": .5, "center_y": .5}
                                    ))
        self.save.add_widget(MDLabel(text=" Сохранено"))
        self.save_button = False


class WindowManager(ScreenManager):
    pass


class FuelApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.settings = settings
        self.money = money

    def build(self):
        return WindowManager()

    def change_money(self, val):
        global money
        settings["money"] = {"money": val}
        money = appdata.money[settings["money"]["money"]]
        self.dialog.dismiss()

    def show_simple_dialog(self, cls: dict):
        if cls["cls"] == "lang":
            clas = LangDia
        else:
            clas = MoneyDia
        self.dialog = MDDialog(content_cls=clas(), type="custom", radius=[15, 15, 15, 15])
        self.dialog.open()


if __name__ == '__main__':
    settings = JsonStore("settings.json")  # configs from json
    refs = {'MainWindow': None}  # reference on screen objects
    money = appdata.money[settings["money"]["money"]]  # actual money info
    FuelApp().run()
