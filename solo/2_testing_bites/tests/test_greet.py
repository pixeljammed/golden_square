from lib.greet import greet

def test_greet():
    actual = greet("Milo")
    expected = "Hello, Milo!"
    actual == expected