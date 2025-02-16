import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_normal_string():
    """Test replacing spaces in a normal string."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_multiple_spaces():
    """Test replacing multiple consecutive spaces."""
    assert replace_spaces_with_underscores("hello   world") == "hello___world"

def test_replace_spaces_leading_trailing_spaces():
    """Test replacing leading and trailing spaces."""
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_empty_string():
    """Test replacing spaces in an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_no_spaces():
    """Test a string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_invalid_input():
    """Test raising TypeError for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)