from lib.report_length import report_length
def test_report_length():
    actual = report_length("Poop")
    expected = "This string was 4 characters long."
    assert actual == expected