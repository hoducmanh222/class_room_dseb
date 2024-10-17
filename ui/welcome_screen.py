from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.welcome_label = Label(text="Hello, User!")
        self.layout.add_widget(self.welcome_label)

        self.timetable_button = Button(text="View Timetable")
        self.timetable_button.bind(on_press=self.view_timetable)
        self.layout.add_widget(self.timetable_button)

        self.deadlines_button = Button(text="View Deadlines")
        self.deadlines_button.bind(on_press=self.view_deadlines)
        self.layout.add_widget(self.deadlines_button)

    def view_timetable(self, instance):
        self.manager.current = 'timetable'

    def view_deadlines(self, instance):
        self.manager.current = 'deadlines'