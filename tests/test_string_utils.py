import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores_basic():
    """Test basic space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_with_underscores_multiple_spaces():
    """Test replacing multiple spaces in a string."""
    assert replace_spaces_with_underscores("hello   world  test") == "hello___world__test"

def test_replace_spaces_with_underscores_edge_cases():
    """Test edge cases like empty string and string with no spaces."""
    assert replace_spaces_with_underscores("") == ""
    assert replace_spaces_with_underscores("nospaceshere") == "nospaceshere"

def test_replace_spaces_with_underscores_leading_trailing_spaces():
    """Test strings with leading and trailing spaces."""
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_with_underscores_invalid_input():
    """Test error handling for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)