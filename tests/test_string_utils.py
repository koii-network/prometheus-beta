import pytest
from src.string_utils import replace_spaces_with_underscores

def test_basic_space_replacement():
    """Test basic space replacement works correctly."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_multiple_spaces():
    """Test that multiple spaces are correctly replaced."""
    assert replace_spaces_with_underscores("  multiple   spaces  ") == "__multiple___spaces__"

def test_empty_string():
    """Test that an empty string returns an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_no_spaces():
    """Test a string with no spaces remains unchanged."""
    assert replace_spaces_with_underscores("nospaceshere") == "nospaceshere"

def test_input_type_validation():
    """Test that a TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
        replace_spaces_with_underscores(None)