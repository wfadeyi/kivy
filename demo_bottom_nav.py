from kivy.lang import Builder
from kivymd.app import MDApp

# writing the kv lang code

KV = '''

# declare layout/screen
MDScreen:
    # create space nav bottom
    MDBottomNavigation:
        panel_color: 1, 0, 0,1
        text_color_active: 0,1,0,1
    
        # nav button on bottom of screen
        MDBottomNavigationItem:
            name: 'screen1'
            text: 'pytho'
            icon: 'language-python'

            # triggered when screen1 selected
            # creates label
            MDLabel:
                text:'Python'
                halign: 'center'

        # nav button bottom of screen
        MDBottomNavigationItem:
            name: 'screen2'
            text: 'java'
            icon: 'language-java'

            #triggered when screen2 selected
            #creates label
            MDLabel:
                text: 'Java'
                halign: 'center'

        # nav button bottom of screen
        MDBottomNavigationItem:
            name: 'screen3'
            text: 'cpp'
            icon: 'language-cpp'

            #triggered when screen2 selected
            #creates label
            MDLabel:
                text: 'CPP'
                halign: 'center'
'''

# App class
class BottomNavApp(MDApp):
    def build(self):
        # load kv lang in code
        screen = Builder.load_string(KV)

        return screen

BottomNavApp().run()
