from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from deadline import Deadline

class AddDeadlineScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.name_input = TextInput(hint_text="Name")
        self.layout.add_widget(self.name_input)

        self.content_input = TextInput(hint_text="Content")
        self.layout.add_widget(self.content_input)

        self.date_input = TextInput(hint_text="Date (e.g., 2023-10-01)")
        self.layout.add_widget(self.date_input)

        self.add_button = Button(text="Add Deadline")
        self.add_button.bind(on_press=self.add_deadline)
        self.layout.add_widget(self.add_button)

        self.back_button = Button(text="Back")
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)

    def add_deadline(self, instance):
        name = self.name_input.text
        content = self.content_input.text
        date = self.date_input.text

        if name and content and date:
            new_deadline = Deadline(name, content, date)
            self.manager.db.add_deadline(new_deadline)
            self.manager.current = 'deadlines'

    def go_back(self, instance):
        self.manager.current = 'deadlines'