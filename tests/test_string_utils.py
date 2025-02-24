import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores_basic():
    """Test basic string space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_with_underscores_multiple_spaces():
    """Test replacing multiple spaces in a string."""
    assert replace_spaces_with_underscores("hello  world  test") == "hello__world__test"

def test_replace_spaces_with_underscores_leading_trailing_spaces():
    """Test replacing spaces at the beginning and end of a string."""
    assert replace_spaces_with_underscores(" hello world ") == "_hello_world_"

def test_replace_spaces_with_underscores_empty_string():
    """Test replacing spaces in an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_with_underscores_no_spaces():
    """Test a string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_with_underscores_invalid_input():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
    
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(None)