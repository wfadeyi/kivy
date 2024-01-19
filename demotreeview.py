from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.treeview import TreeView, TreeViewNode


class MyNode(BoxLayout):

    def __init__(self, **kwargs):
        text = kwargs.pop('text', 'None')
        super(MyNode, self).__init__(**kwargs)
        self.orientation = 'horizontal'

        # make height reasonable
        self.size_hint_y = None
        self.height = dp(25)

        # make the parts of the node
        self.lbl = Label(text=text, size_hint_x=0.2)
        self.chkbx = CheckBox(size_hint_x=0.1, color=(1, 1, 1, 3.5))  # alpha=3.5 to make it more visible
        self.txtinpt = TextInput(multiline=False, font_size=15, padding=[6, 3, 6, 0])

        # add the parts to the BoxLayout
        self.add_widget(self.lbl)
        self.add_widget(self.chkbx)
        self.add_widget(self.txtinpt)


class MyTreeNode(MyNode, TreeViewNode):
    pass


class MyTreeView(TreeView):
    def __init__(self):
        super(MyTreeView, self).__init__()
        self.add_node(MyTreeNode(text='node 1'))
        node2 = self.add_node(MyTreeNode(text='node 2'))
        self.add_node(MyTreeNode(text='node 3'), node2)
        self.add_node(MyTreeNode(text='node 4'), node2)


class TreeViewApp(App):
    def build(self):
        return MyTreeView()


if __name__ == '__main__':
    TreeViewApp().run()
