from lib.note import includes_todo
import pytest


def test_includes_todo():
    # given a note containing "#TODO", returns true
    assert includes_todo("#TODO buy milk") == True

    # given a note that does not contain "#TODO", returns false
    assert includes_todo("drink tea") == False

    # given a note that contains multiple "#TODO"s, returns true
    assert includes_todo("#TODO learn to test-drive my code #TODO") == True

    # given a note that contains "#TODO" in the middle of the string, returns true
    assert includes_todo("learn to test-drive #TODO my code") == True

    # given an empty string, returns false
    assert includes_todo("") == False

    # given None, returns a type error??
    with pytest.raises(Exception) as e:
        includes_todo(None) == TypeError
    error_message = str(e.value)
    assert error_message == "you did not give me a string !! >_<"
