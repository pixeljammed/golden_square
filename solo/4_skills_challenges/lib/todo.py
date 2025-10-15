class ToDoList():
    def __init__(self):
        self.tdl = []

    def add(self, todo):
        self.tdl.append(todo)

    def view(self):
        return self.tdl

    def complete(self, todo):
        self.tdl.remove(todo)
