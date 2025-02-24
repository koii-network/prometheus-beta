import pytest
from src.replace_spaces import replace_spaces_with_underscores

def test_replace_spaces_basic():
    """Test basic space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_multiple():
    """Test replacing multiple spaces."""
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_leading_trailing():
    """Test spaces at beginning and end of string."""
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_empty_string():
    """Test empty string input."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_no_spaces():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_invalid_input():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)