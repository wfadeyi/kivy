# Make accordion in kivy with .kv file

import kivy

from kivy.app import App

from kivy.uix.accordion import Accordion, AccordionItem

from kivy.uix.label import Label

# Create the Accordion class whose work is done in .kv file

class MyAccordion(Accordion):
    pass

class DemoAccordion2App(App):

    def build(self):

    
        return MyAccordion()

    
if __name__ == '__main__':
    DemoAccordion2App().run()
