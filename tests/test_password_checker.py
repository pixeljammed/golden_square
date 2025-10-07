import pytest
from lib.password_checker import *

def test_length_under_8():
    passcheck = PasswordChecker()
    with pytest.raises(Exception) as e:
        passcheck.check("sigma")
    message = str(e.value)
    assert message == "Invalid password, must be 8+ characters."

def test_length_over_8():
    passcheck = PasswordChecker()
    assert passcheck.check("diddyblud") == True