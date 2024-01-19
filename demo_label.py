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
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen

class Demo_Label(MDApp):
    def build(self):
        # define screen
        screen = Screen()

        #first label
        lbl1 = MDLabel(text='Welcome', pos_hint={'center_x':0.8,
                                                 'center_y': 0.8},
                       theme_text_color='Custom',
                       text_color=(0.5, 0.5, 1),
                       font_style='Caption')

        lbl2 = MDLabel(text='Welcome', pos_hint={'center_x':0.8,
                                                 'center_y': 0.5},
                       theme_text_color='Custom',
                       text_color=(0.5, 0.5, 1),
                       font_style='H2')

        lbl3 = MDLabel(text='Welcome', pos_hint={'center_x':0.8,
                                                 'center_y': 0.2},
                       theme_text_color='Custom',
                       text_color=(0.5, 0.5, 1),
                       font_style='H1')

        screen.add_widget(lbl1)
        screen.add_widget(lbl2)
        screen.add_widget(lbl3)
        return screen

if __name__ == '__main__':
    Demo_Label().run()

