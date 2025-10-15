# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

Don't worry about user input & output here.

## 2. Design the Class Interface

```python
# EXAMPLE

class ToDoList:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        pass # No code here yet

    def add(self, task):
        # Parameters:
        #   task: string representing a single todo
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the todo to the todo list
        pass

    def view(self):
        # Parameters:
        #   none
        # Returns:
        #   the list of todos
        # Side-effects
        #   none
        pass # No code here yet

    def complete(self, task):
        # Returns:
        #   none
        # Side-effects:
        #   removes task from the list
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
add()
adds an todo to the todo list
"""
todo = ToDoList()
todo.add("Walk the dog")

"""
view()
view the todo list
"""
todo = ToDoList("Kay")
todo.add("Play L4D2")
todo.add("Fart and poop")
todo.add("Go to a public place and start screaming for no reason")
todo.view()

"""
complete()
removes a todo from the todo list
"""
todo = ToDoList()
todo.add("Jeet everyone")
todo.complete("Jeet everyone")
```

## 4. Implement the Behaviour

fuqu