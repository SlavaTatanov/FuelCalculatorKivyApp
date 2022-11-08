from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFlatButton
from kivymd.uix.label import MDIcon, MDLabel
from kivymd.uix.datatables import MDDataTable
from calculating import calculating, names
import appdata
import data


class LangDia(BoxLayout):
    pass


class MoneyDia(BoxLayout):
    @staticmethod
    def upd(date):
        """
        Changing secondary text label on settings screen (money changing dialog)
        """
        refs['MainWindow'].set_money.secondary_text = date  # in kv file


class MainWindow(Screen):

    def __new__(cls, *args, **kwargs):
        """
        Adds a reference to an object to the list of references
        """
        ref = super().__new__(cls)
        refs["MainWindow"] = ref
        return ref

    def __init__(self, **kwargs):
        """
        The button parameter checks if there is already a button,
        if it already exists, it will not allow adding extra ones
        """
        super().__init__(**kwargs)
        self.save_button = False

    def up_peoples(self, x):
        """
        Increases/decreases the text label with the number of people.
        Checks that the number is at least 1
        """
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
                                                               on_press=lambda slf: self.save_result(res)))

        else:
            self.result.text = f'{res}'

    def save_result(self, obj):
        """
        Saves the result of the calculation to the database, if the record already exists, reports this,
        the 'obj.save' function returns false if the record to the database is not successful
        """
        self.save.clear_widgets()
        if obj.save():
            self.save.add_widget(MDIcon(icon="check-bold",
                                        pos_hint={"center_x": .5, "center_y": .5}))
            self.save.add_widget(MDLabel(text=" Сохранено"))
        else:
            self.save.add_widget(MDIcon(icon="alert",
                                        pos_hint={"center_x": .5, "center_y": .5}))
            self.save.add_widget(MDLabel(text=" Существует"))
        self.save_button = False

    def data_table(self):
        datatable = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                size_hint=(1, 1),
                                check=False,
                                use_pagination=True,
                                pagination_menu_pos='auto',
                                background_color=(0.0, 0.749, 1.0, .4),
                                column_data=[("Дата", 20), ("Км", 13), ("Лит", 17), ("Цена", 20)],
                                )
        self.data_tab.add_widget(datatable)


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

    def show_simple_dialog(self, cls):
        if cls == "lang":
            clas = LangDia
        else:
            clas = MoneyDia
        self.dialog = MDDialog(content_cls=clas(), type="custom", radius=[15, 15, 15, 15])
        self.dialog.open()

    def show_quest(self, title, text, button1, button2):
        self.dialog = MDDialog(title=title,
                               text=text,
                               buttons=[MDFlatButton(text=button1,
                                                     on_press=lambda slf:data.Trip.clear_data(self.dialog)),
                                        MDFlatButton(text=button2,
                                                     on_press=lambda slf:self.dialog.dismiss())])
        self.dialog.open()


if __name__ == '__main__':
    settings = JsonStore("settings.json")  # configs from json
    refs = {'MainWindow': None}  # reference on screen objects
    money = appdata.money[settings["money"]["money"]]  # actual money info
    FuelApp().run()
