class Contact:
    def __init__(self):
        contacts = {}

    def add(self, name, number):
        self.contacts.update(name, number)

    def remove(self, name):
        self.contacts.remove(name)

    def get(self, name):
        pass

    def all(self):
        return self.contacts