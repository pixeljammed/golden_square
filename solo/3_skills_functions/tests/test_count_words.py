from lib.count_words import *
"""
count_words()
Returns the number of words in a sentence
"""
def test_count_words():
    actual = count_words("Left for Dead is the best zombie game of all time.")
    expected = 11
    assert actual == expected