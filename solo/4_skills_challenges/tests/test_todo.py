from lib.todo import ToDoList

def test_create_todo_list():
    td = ToDoList()
    assert type(td) == ToDoList
    assert td.tdl == []

def test_add_todo():
    td = ToDoList()
    td.add("Drink 1,000,000 beers")
    assert td.tdl == ["Drink 1,000,000 beers"]

def test_view_todo():
    td = ToDoList()
    td.add("Poop all over the walls")
    td.add("Pee everywhere on the floor")
    assert td.view() == ["Poop all over the walls", "Pee everywhere on the floor"]

def test_complete_todo():
    td = ToDoList()
    td.add("Eat")
    td.add("Sleep")
    td.add("Clash Royale")
    td.add("Repeat")
    td.complete("Eat")
    td.complete("Sleep")
    assert td.view() == ["Clash Royale", "Repeat"]