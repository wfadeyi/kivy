import kivy

from kivy.app import App
from kivy.uix.tabbedpanel import TabbedPanel

from kivy.uix.floatlayout import FloatLayout

# Create Tabbed class
class Tab(TabbedPanel):
    pass

#create App class
class TabbedPanelApp(App):
    def build(self):
        return Tab()

if __name__ == '__main__':
    TabbedPanelApp().run()

    
