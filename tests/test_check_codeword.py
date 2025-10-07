from lib.codeword import check_codeword

def test_correct_codeword():
    assert check_codeword("horse") == "Correct! Come in."

def test_close_codeword():
    assert check_codeword("hawke") == "Close, but nope."

def test_wrong_codeword():
    assert check_codeword("poopy") == "WRONG!"