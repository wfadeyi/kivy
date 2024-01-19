import kivy
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
    def build(self):

        btn = Button(text ='Press me',
                     font_size ='20sp',
                     background_color = (1,1,1,1),
                     color=(1,1,1,1),
                     size=(32,32),
                     size_hint=(.2,.2),
                     pos=(300,250))

        btn.bind(on_press=self.callbackfunc)

        
        return btn
    def callbackfunc(self,event):
        print('button clicked')
        

ButtonApp().run()
