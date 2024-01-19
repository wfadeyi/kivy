##import kivy
##from kivy.app import App
##from kivy.uix.label import Label
##
##class MainApp(App):
##    def build(self):
##        return Label(text="Hello, World!")
##
##MainApp().run()

from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons

class DemoApp(MDApp):
    def build(self):

        screen = Screen()

        btn1 = MDFlatButton(text='Hello 1', pos_hint={'center_x': 0.5,
                                                      'center_y': 0.8})
        btn2 = MDFloatingActionButton(icon='android', pos_hint={'center_x': 0.5,
                                                      'center_y': 0.5},)

        screen.add_widget(btn1)
        screen.add_widget(btn2)

        return screen


DemoApp().run()
