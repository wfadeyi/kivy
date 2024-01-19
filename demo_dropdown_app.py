import kivy

from kivy.app import App

from kivy.uix.dropdown import DropDown

from kivy.uix.button import Button

# Alternative way to run kivy app
from kivy.base import runTouchApp

# Create dropdown with 10 buttons

dropdown = DropDown()

for index in range(10):
    # Add button in dropdown list
    btn = Button(text=f'Value {index}', size_hint_y = None, height=40)

    # Bind button to show the text when selected

    btn.bind(on_release = lambda btn: dropdown.select(btn.text))

    # Add button inside dropdown

    dropdown.add_widget(btn)

# Create a main big button

mainbutton = Button(text='Hello', size_hint = (None, None), pos = (350,300))

# Show dropdown menu when main button is released

mainbutton.bind(on_release=dropdown.open)

# Listen for the selection in the dropdown list and assign the data to the button text

dropdown.bind(on_select= lambda instance, x: setattr(mainbutton, 'text', x))

runTouchApp(mainbutton)
