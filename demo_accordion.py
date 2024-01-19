# Make accordion in kivy

import kivy

from kivy.app import App

from kivy.uix.accordion import Accordion, AccordionItem

from kivy.uix.label import Label

class DemoAccordionApp(App):

    def build(self):

        root = Accordion()
        root = Accordion(min_space = 60)
        root = Accordion(orientation='vertical')

        # Add text to each accordion
        for x in range(5):
            item = AccordionItem(title = f'Title {x}')
            item.add_widget(Label(text='Chemistry\n' *4))
            root.add_widget(item)

        return root
if __name__ == '__main__':
    DemoAccordionApp().run()
