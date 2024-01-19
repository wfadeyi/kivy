# demo for lesson/testing application GUI in kivy
import englishmain as eng
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

class SchoolHomeApp(App):

    def build(self):

        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal')

        lbl_intro = Label(text='Choose a subject')

        hbox.add_widget(lbl_intro)

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')
                         
        btn_english = Button(text='English Language')
        btn_math = Button(text='Mathematics')
        btn_science = Button(text='Basic Science')
        btn_home_econs = Button(text='Home Economics')

        vbox.add_widget(btn_english)
        vbox.add_widget(btn_math)
        vbox.add_widget(btn_science)
        vbox.add_widget(btn_home_econs)

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox

class SubjectHomeApp(App):

    def build(self):

        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal')

        lbl_intro = Label(text='What do you want to do today?')

        hbox.add_widget(lbl_intro)

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')
                         
        btn_lesson = Button(text='Watch a video lesson')
        btn_test = Button(text='Take a test')

        vbox.add_widget(btn_lesson)
        vbox.add_widget(btn_test)

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox

class TopicsHomeApp(App):

    def build(self):

        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal')

        lbl_intro = Label(text='Choose a topic')

        hbox.add_widget(lbl_intro)

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')

        for topic in range(4):               
            btn_topic = Button(text=f'Topic {topic}')
            vbox.add_widget(btn_topic)
        

        

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox

class LessonHomeApp(App):

    def build(self):

        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal')

        lbl_intro = Label(text='Current Lesson Topic')

        hbox.add_widget(lbl_intro)

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')
                         
        btn_lesson = Button(text='Watch a video lesson')
        btn_test = Button(text='Do lesson exercises')

        vbox.add_widget(btn_lesson)
        vbox.add_widget(btn_test)

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox


class LessonHomeApp(App):

    def build(self):

        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal')

        lbl_intro = Label(text='Current Lesson Topic')

        hbox.add_widget(lbl_intro)

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')
                         
        btn_lesson = Button(text='Watch a video lesson')
        btn_test = Button(text='Do lesson exercises')

        vbox.add_widget(btn_lesson)
        vbox.add_widget(btn_test)

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox



# Checkbox class
# Container class for the widgets in the app
# Equivalent to a checkbox group

class CheckBoxes(GridLayout):

    def __init__(self, **kwargs):
        super(CheckBoxes, self).__init__(**kwargs)

        #2 columns in grid layout

        self.cols = 2

        #Add checkbox, widget, and labels

        self.add_widget(Label(text='Topic 1'))
        self.active1 = CheckBox()
##        self.active1.group = 'topics'
        self.add_widget(self.active1)

        self.add_widget(Label(text='Topic 2'))
        self.active2 = CheckBox()
##        self.active2.group = 'topics'
        self.add_widget(self.active2)

        self.add_widget(Label(text='Topic 3'))
        self.active3 = CheckBox()
        self.add_widget(self.active3)

##        # Add label to screen to read selection
##
##        self.lbl_active = Label(text = 'Checkbox is on')
##        self.add_widget(self.lbl_active)
##
##        # Attach a callback
##
##        self.active1.bind(active = self.on_checkbox_Active)
##
##    def on_checkbox_Active(self, checkboxInstance, isActive):
##        if isActive:
##            self.lbl.active.text = 'Checked'
##            print('Checked')
##        else:
##            self.lbl.active.text = 'Unchecked'
##            print('Unchecked')

class QuizHomeApp(App):

    def build(self):


        # master container hosting other containers
        superbox = BoxLayout(orientation='vertical')

        # horizontal layout box
        hbox = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))

        lbl_input = Label(text='Enter number of questions wanted (maximum of 20)', size_hint=(0.3, 0.5))
        txt_input = TextInput(multiline=False, size_hint=(0.3, 0.5))

        hbox.add_widget(lbl_input)
        hbox.add_widget(txt_input)

        

        # vertical layout box
        vbox = BoxLayout(orientation='vertical')

        lbl_select = Label(text='Select the topics you want')

        cb_group = CheckBoxes()

        vbox.add_widget(lbl_select)
        vbox.add_widget(cb_group)
                         
        btn_start = Button(text='Start test')

        vbox.add_widget(btn_start)

        # Add all to superbox

        superbox.add_widget(hbox)
        superbox.add_widget(vbox)

        return superbox


class QuizApp(App):
    def build(self):
        pass
        




    
if __name__ == '__main__':

    QuizHomeApp().run()
                         
                         

        
