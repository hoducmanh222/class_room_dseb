from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from subject import Subject

class AddSubjectScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        self.name_input = TextInput(hint_text="Name")
        self.layout.add_widget(self.name_input)

        self.lecturer_input = TextInput(hint_text="Lecturer")
        self.layout.add_widget(self.lecturer_input)

        self.room_input = TextInput(hint_text="Room")
        self.layout.add_widget(self.room_input)

        self.day_spinner = Spinner(
            text='Select Day',
            values=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
        )
        self.layout.add_widget(self.day_spinner)

        self.time_input = TextInput(hint_text="Time (e.g., 10:00 AM)")
        self.layout.add_widget(self.time_input)

        self.length_input = TextInput(hint_text="Length")
        self.layout.add_widget(self.length_input)

        self.add_button = Button(text="Add Subject", background_normal='', background_color=(0, 1, 0, 1))
        self.add_button.bind(on_press=self.add_subject)
        self.layout.add_widget(self.add_button)

        self.back_button = Button(text="Back to Menu", size_hint=(None, None), size=(150, 50), background_normal='', background_color=(0.8, 0.8, 0.8, 1))
        self.back_button.bind(on_press=self.go_back)
        self.layout.add_widget(self.back_button)

    def add_subject(self, instance):
        name = self.name_input.text
        lecturer = self.lecturer_input.text
        room = self.room_input.text
        day = self.day_spinner.text
        time = self.time_input.text
        length = self.length_input.text

        if name and lecturer and room and day != 'Select Day' and time and length:
            full_time = f"{day} {time}"
            new_subject = Subject(name, lecturer, room, full_time, length)
            self.manager.db.add_subject(new_subject)
            self.manager.current = 'timetable'

    def go_back(self, instance):
        self.manager.current = 'timetable'