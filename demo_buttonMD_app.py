from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton

class ButtonMDApp(MDApp):

    def build(self):

        screen = Screen()

        btn = MDRectangleFlatButton(text='Submit',
                                    pos_hint={'center_x': 0.5, 'center_y' : 0.3},
                                    on_release=self.btnfunc)
        screen.add_widget(btn)

        return screen
    def btnfunc(self, obj):
        print('Button pressed')

if __name__ =='__main__':
    ButtonMDApp().run()
