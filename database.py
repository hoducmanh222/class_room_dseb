import json

class Database:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.data = {'subjects': [], 'deadlines': []}
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.save()

    def save(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_subject(self, subject):
        self.data['subjects'].append(subject.__dict__)
        self.save()

    def remove_subject(self, subject_name):
        self.data['subjects'] = [s for s in self.data['subjects'] if s['name'] != subject_name]
        self.save()

    def add_deadline(self, deadline):
        self.data['deadlines'].append(deadline.__dict__)
        self.save()

    def remove_deadline(self, deadline_name):
        self.data['deadlines'] = [d for d in self.data['deadlines'] if d['name'] != deadline_name]
        self.save()