import pytest
from src.lowercase_with_spaces import lowercase_with_spaces

def test_basic_lowercase():
    assert lowercase_with_spaces("Hello World") == "hello world"

def test_mixed_case():
    assert lowercase_with_spaces("PythonProgramming") == "python programming"

def test_with_punctuation():
    assert lowercase_with_spaces("Hello, World!") == "hello world"

def test_with_mixed_special_chars():
    assert lowercase_with_spaces("Python_is-AWESOME") == "python is awesome"

def test_empty_string():
    assert lowercase_with_spaces("") == ""

def test_only_special_chars():
    assert lowercase_with_spaces("!@#$%^&*()") == ""

def test_invalid_input_type():
    with pytest.raises(TypeError):
        lowercase_with_spaces(123)
    with pytest.raises(TypeError):
        lowercase_with_spaces(None)