from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import ListProperty


class DynamicLabelsApp(App):
    """Main program - Kivy app to demo dynamic label creation."""
    names = ListProperty ()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - list of names
        self.names = ["France", "China", "Singapore", "Korea"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each name in the list
            temp_label = Label(text=name)
            # add the label to the "main" layout widget
            self.root.ids.main.add_widget(temp_label)


DynamicLabelsApp().run()
