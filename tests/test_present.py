import pytest
from lib.present import *

def test_wrap_with_content():
    present = Present()
    present.wrap(10)
    assert present.unwrap() == 10

def test_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped"

def test_wrapping_already_wrapped():
    present = Present()
    present.wrap(44)
    with pytest.raises(Exception) as e:
        present.wrap(66)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped"