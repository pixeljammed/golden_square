from lib.verify_sentence import *
"""
verify_sentence()
Returns true if the first character is a capital, and the last character is one of ".", "!" or "?"
"""
def test_verify_sentence():
    actual = verify_sentence("Eat your greens!")
    expected = True
    assert actual == expected