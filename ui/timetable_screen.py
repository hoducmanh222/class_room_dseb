from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.image import Image
from datetime import datetime

class TimetableScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.add_widget(self.layout)

        with self.canvas.before:
            Color(1, 0.9, 0.9, 1)  # Pastel pink background
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
            self.bind(pos=self.update_rect, size=self.update_rect)

        # Date Navigation Bar
        self.date_nav_bar = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        self.layout.add_widget(self.date_nav_bar)
        self.create_date_nav_bar()

        self.subject_label = Label(text="Today's Subjects", size_hint_y=None, height=30, color=(0, 0, 0, 1))
        self.layout.add_widget(self.subject_label)

        # Scrollable subject list
        scroll_view = ScrollView(size_hint=(1, 1))
        self.subject_list = BoxLayout(orientation='vertical', spacing=20, size_hint_y=None)
        self.subject_list.bind(minimum_height=self.subject_list.setter('height'))
        scroll_view.add_widget(self.subject_list)
        self.layout.add_widget(scroll_view)

        # Button layout for "Add" and "Back to Menu"
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=60, spacing=10)
        self.layout.add_widget(button_layout)

        # Spacers to center the buttons
        button_layout.add_widget(BoxLayout(size_hint_x=0.5))

        add_button_layout = BoxLayout(orientation='vertical', size_hint=(None, None), size=(50, 50))
        self.add_subject_button = Button(text="+", size_hint=(None, None), size=(50, 50), background_normal='', background_color=(0, 1, 0, 1))
        self.add_subject_button.bind(on_press=self.add_subject)
        add_button_layout.add_widget(self.add_subject_button)
        button_layout.add_widget(add_button_layout)

        self.back_button = Button(text="Back to Menu", size_hint=(None, None), size=(150, 50), background_normal='', background_color=(0.8, 0.8, 0.8, 1))
        self.back_button.bind(on_press=self.go_back)
        button_layout.add_widget(self.back_button)

        button_layout.add_widget(BoxLayout(size_hint_x=0.5))  # Spacer

    def create_date_nav_bar(self):
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        today = datetime.now().strftime('%A')
        for day in days:
            btn = Button(text=day, background_color=(0, 1, 0, 1) if day == today else (1, 1, 1, 1))
            btn.bind(on_press=self.change_day)
            self.date_nav_bar.add_widget(btn)

    def change_day(self, instance):
        self.subject_list.clear_widgets()
        selected_day = instance.text
        subjects_today = [s for s in self.manager.db.data['subjects'] if s['time'].startswith(selected_day)]
        subjects_today.sort(key=lambda x: x['time'])
        for subject in subjects_today:
            self.add_subject_card(subject)

    def on_enter(self):
        self.subject_list.clear_widgets()
        today = datetime.now().strftime('%A')
        subjects_today = [s for s in self.manager.db.data['subjects'] if s['time'].startswith(today)]
        subjects_today.sort(key=lambda x: x['time'])
        for subject in subjects_today:
            self.add_subject_card(subject)

    def add_subject_card(self, subject):
        card = BoxLayout(orientation='horizontal', padding=10, size_hint_y=None, height=150, spacing=10)
        with card.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = RoundedRectangle(size=card.size, pos=card.pos, radius=[10])
            card.bind(pos=self.update_rect, size=self.update_rect)

        info_layout = BoxLayout(orientation='vertical', spacing=5, size_hint_x=1)

        # Function to create an info row with icon and label
        def add_info_row(icon_path, text):
            row_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=30, spacing=10, padding=[10, 0])
            icon = Image(source=icon_path, size_hint=(None, None), size=(30, 30))
            label = Label(text=text, color=(0, 0, 0, 1), size_hint_x=1)
            row_layout.add_widget(icon)
            row_layout.add_widget(label)
            info_layout.add_widget(row_layout)

        # Add subject details with icons
        add_info_row(r'C:\Users\HP\PycharmProjects\pythonProject\my_website\classroom_app\5231939.png', f"Name: {subject['name']}")
        add_info_row(r'C:\Users\HP\PycharmProjects\pythonProject\my_website\asssistant_auto\human.png', f"Lecturer: {subject['lecturer']}")
        add_info_row(r'C:\Users\HP\PycharmProjects\pythonProject\my_website\asssistant_auto\building.png', f"Room: {subject['room']}")
        add_info_row(r'C:\Users\HP\PycharmProjects\pythonProject\my_website\asssistant_auto\clock.png', f"Time: {subject['time']}")
        add_info_row(r'C:\Users\HP\PycharmProjects\pythonProject\my_website\asssistant_auto\clock.png', f"Length: {subject['length']}")

        card.add_widget(info_layout)

        remove_button = Button(text="-", size_hint=(None, None), size=(30, 30), background_normal='', background_color=(1, 0, 0, 1))
        remove_button.bind(on_press=lambda x: self.confirm_remove_subject(subject['name']))
        card.add_widget(remove_button)

        self.subject_list.add_widget(card)

    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def confirm_remove_subject(self, subject_name):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=f"Are you sure you want to remove {subject_name}?", color=(0, 0, 0, 1)))
        confirm_button = Button(text="Yes", background_normal='', background_color=(0, 1, 0, 1))
        cancel_button = Button(text="No", background_normal='', background_color=(1, 0, 0, 1))
        content.add_widget(confirm_button)
        content.add_widget(cancel_button)

        popup = Popup(title="Confirm Remove", content=content, size_hint=(0.5, 0.5))
        confirm_button.bind(on_press=lambda x: self.remove_subject(subject_name, popup))
        cancel_button.bind(on_press=popup.dismiss)
        popup.open()

    def remove_subject(self, subject_name, popup):
        self.manager.db.remove_subject(subject_name)
        self.on_enter()  # Refresh the list
        popup.dismiss()

    def add_subject(self, instance):
        self.manager.current = 'add_subject'

    def go_back(self, instance):
        self.manager.current = 'welcome'
