import pytest
from lib.present import *

def wrap_and_then_unwrap():
    present = Present()
    present.wrap(69)
    assert present.unwrap() == 69

def test_unwrap_without_wrapped_first():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    message = str(e.value)
    assert message == "No contents have been wrapped."

def test_already_wrapped():
    present = Present()
    present.wrap(1337)
    with pytest.raises(Exception) as e:
        present.wrap(9001)
    message = str(e.value)
    assert message == "A contents has already been wrapped."

def test_already_wrapped_preserves_value():
    present = Present()
    present.wrap(1337)
    with pytest.raises(Exception) as e:
        present.wrap(9001)
    assert present.unwrap == 1337