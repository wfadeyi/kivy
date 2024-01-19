import kivy
import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


# Declare colors

red = [1, 0, 0, 1]
green = [0, 1, 0, 1]
blue = [0, 0, 1, 1]
purple = [1, 0, 1, 1]


class BoxLayoutApp(App):

    def build(self):
        # To position oriented widgets again in the proper orientation
        # use of vertical orientation to set all widgets

        superbox = BoxLayout(orientation = 'vertical')

        # Position widgets next to each other with horizontal layout

        hbox = BoxLayout(orientation='horizontal')

        colors = [red, green, blue, purple]

        btn1 = Button(text='One',
                      background_color = random.choice(colors),
                      font_size = 32,
                      size_hint = (0.7, 1))
        btn2 = Button(text='Two',
                      background_color = random.choice(colors),
                      font_size = 32,
                      size_hint = (0.7, 1))

        hbox.add_widget(btn1)
        hbox.add_widget(btn2)

        # Position widgets vertically

        vbox = BoxLayout(orientation='vertical')

        btn3 = Button(text='Three',
                      background_color = random.choice(colors),
                      font_size = 32,
                      size_hint = (1, 10))
        btn4 = Button(text='Four',
                      background_color = random.choice(colors),
                      font_size = 32,
                      size_hint = (1, 15))

        vbox.add_widget(btn3)
        vbox.add_widget(btn4)

        # Use superbox to align the oriented widgets

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox

BoxLayoutApp().run()
