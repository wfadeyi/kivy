import kivy
from kivy.app import App

from kivy.uix.label import Label

# Float layout

from kivy.uix.floatlayout import FloatLayout

# Scatter for widgets manipulation on multitouch

from kivy.uix.scatter import Scatter

# TextInput

from kivy.uix.textinput import TextInput

# Box Layout

from kivy.uix.boxlayout import BoxLayout


class DemoTxtInputApp(App):
    def build(self):
        b = BoxLayout(orientation='vertical')

        t = TextInput(font_size=50,
                      size_hint_y=None,
                      height=100)

        f = FloatLayout()

        # Scatter to move Text about
        s = Scatter()

        l = Label(text='Hello',
                  font_size=50)

        # Add scatter to floatlayout
        f.add_widget(s)

        # Add label to scatter
        s.add_widget(l)

        # Add text to boxlayout

        b.add_widget(t)

        # Add floatlayout to boxlayout

        b.add_widget(f)

        # Bind text with label

        t.bind(text=l.setter('text'))

        # return box layout

        return b

if __name__ =='__main__':
    DemoTxtInputApp().run()

               

    
