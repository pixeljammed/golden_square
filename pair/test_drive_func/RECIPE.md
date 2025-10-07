# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
def includes_todo(note):
    """Return true if note contains "#TODO", and returns false if not

    Parameters:
        note: a string

    Returns:
        boolean: true for contains "#TODO", false for not

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# given a note containing "#TODO", returns true
includes_todo("#TODO buy milk") == True

# given a note that does not contain "#TODO", returns false
includes_todo("drink tea") == False

# given a note that contains multiple "#TODO"s, returns true
includes_todo("#TODO learn to test-drive my code #TODO") == True

# given a note that contains "#TODO" in the middle of the string, returns true
includes_todo("learn to test-drive #TODO my code") == True

# given an empty string, returns false
includes_todo("") == False

# given None, returns a type error??
includes_todo(None) == TypeError
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
