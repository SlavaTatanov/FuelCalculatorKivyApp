from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.theming import ThemeManager


class Container(GridLayout):

    def up_peoples(self, x):
        peoples = int(self.peoples_lbl.text)
        peoples += x
        if peoples != 0:
            self.peoples_lbl.text = str(peoples)


class FuelApp(MDApp):
    theme_sls = ThemeManager
    title = 'myapp'

    def build(self):
        self.theme_sls.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    FuelApp().run()

