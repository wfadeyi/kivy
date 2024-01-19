import kivy

from kivy.app import App

from kivy.uix.label import Label

class LabelApp(App):
    def build(self):
        lbl = Label(text="[color = ff3333][b]Label[/b] is [/color]\n [color = 3333ff] added on screen[/color]",
                    font_size ='20sp', markup = True)

        lbl2 = Label(text="[b]Bold[/b] [color=3333ff]nonbold text [/color]",
                    font_size ='20sp', markup = True)
        return lbl2
LabelApp().run()


