import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.config import Config

Config.set('graphics', 'resizable', True)

class PopupApp(App):
    def build(self):
        self.layout = GridLayout(cols=1, padding=10)

        self.button = Button(text='Open popup')
        self.layout.add_widget(self.button)

        # Callback for button press
        self.button.bind(on_press = self.onButtonPress)

        return self.layout

    def onButtonPress(self, button):
        layout = GridLayout(cols=1, padding=10)
        popupLabel = Label(text='Click for popup')
        closeButton = Button(text='Close popup')
        layout.add_widget(popupLabel)
        layout.add_widget(closeButton)

        popup = Popup(title='My Popup', content = layout,
                      size_hint=(None, None), size = (200, 200))
        popup.open()

        # Attach close button press with popup dismissal
        closeButton.bind(on_press = popup.dismiss)

if __name__ == '__main__':
    PopupApp().run()
