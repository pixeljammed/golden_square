import pytest
from lib.reminder import *

def test_remind_of_task():
    reminder = Reminder("Milo")
    reminder.remind_me_to("Walk the dog")
    assert reminder.remind() == "Walk the dog, Milo!"

def test_no_task():
    reminder = Reminder("Dax")
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"