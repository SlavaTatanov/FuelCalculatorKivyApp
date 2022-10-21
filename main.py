from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.theming import ThemeManager


class Container(GridLayout):
    pass


class MyApp(MDApp):
    theme_sls = ThemeManager
    title = 'myapp'

    def build(self):
        self.theme_sls.theme_style = 'Light'
        return Container()


if __name__ == '__main__':
    MyApp().run()

