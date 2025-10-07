from lib.snippet import make_snippet

"""
Given a text with 5 or more words, return one 
"""

def test_make_snippet():
    actual = make_snippet("Today I ate some beans and peas!")
    expected = "Today I ate some beans..."
    assert actual == expected