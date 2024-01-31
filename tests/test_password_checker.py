import pytest
from lib.password_checker import *

def test_valid_password():
    checker = PasswordChecker()
    assert checker.check('12345678') == True

def test_invalid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('')
    error_message = str(e.value)
    assert error_message == "invalid password, must be 8+ characters"
