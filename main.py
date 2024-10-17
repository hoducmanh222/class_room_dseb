from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from database import Database
from ui import WelcomeScreen, TimetableScreen, AddSubjectScreen, DeadlinesScreen, AddDeadlineScreen

class ClassroomApp(App):
    def build(self):
        self.db = Database()
        self.screen_manager = ScreenManager()

        self.welcome_screen = WelcomeScreen(name='welcome')
        self.timetable_screen = TimetableScreen(name='timetable')
        self.add_subject_screen = AddSubjectScreen(name='add_subject')
        self.deadlines_screen = DeadlinesScreen(name='deadlines')
        self.add_deadline_screen = AddDeadlineScreen(name='add_deadline')

        self.screen_manager.add_widget(self.welcome_screen)
        self.screen_manager.add_widget(self.timetable_screen)
        self.screen_manager.add_widget(self.add_subject_screen)
        self.screen_manager.add_widget(self.deadlines_screen)
        self.screen_manager.add_widget(self.add_deadline_screen)

        self.screen_manager.db = self.db

        return self.screen_manager

if __name__ == '__main__':
    ClassroomApp().run()