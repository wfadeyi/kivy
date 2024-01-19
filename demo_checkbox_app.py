import kivy

from kivy.app import App

from kivy.uix.widget import Widget

from kivy.uix.label import Label

from kivy.uix.checkbox import CheckBox

from kivy.uix.gridlayout import GridLayout

# Container class for the widgets in the app
# Equivalent to a checkbox group

class check_box(GridLayout):

    def __init__(self, **kwargs):
        super(check_box, self).__init__(**kwargs)

        #2 columns in grid layout

        self.cols = 2

        #Add checkbox, widget, and labels

        self.add_widget(Label(text='Male'))
        self.active1 = CheckBox(active=True)
        self.add_widget(self.active1)

        self.add_widget(Label(text='Female'))
        self.active2 = CheckBox(active=True)
        self.add_widget(self.active2)

        self.add_widget(Label(text='Other'))
        self.active3 = CheckBox(active=True)
        self.add_widget(self.active3)

        # Add label to screen to read selection

        self.lbl_active = Label(text = 'Checkbox is on')
        self.add_widget(self.lbl_active)

        # Attach a callback

        self.active1.bind(active = self.on_checkbox_Active)

    def on_checkbox_Active(self, checkboxInstance, isActive):
        if isActive:
            self.lbl.active.text = 'Checked'
            print('Checked')
        else:
            self.lbl.active.text = 'Unchecked'
            print('Unchecked')

# Main app

class CheckBoxApp(App):
    def build(self):
        return check_box()

if __name__ == '__main__':
    CheckBoxApp().run()

        
