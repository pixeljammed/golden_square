# name_initials("Milo Tekchandani")
# => M.T

from lib.name_initials import name_initials

def test_name_initials():
    actual = name_initials("Milo Tekchandani")
    expected = "M.T"
    assert actual == expected

def test_name_initials_with_middle_name():
    actual = name_initials("Milo Dhiren Tekchandani")
    expected = "M.T"
    assert actual == expected

def test_name_initials_with_middle_names():
    actual = name_initials("Milo I Eat Bricks Tekchandani")
    expected = "M.T"
    assert actual == expected