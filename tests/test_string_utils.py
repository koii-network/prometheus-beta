import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_basic():
    """Test basic space replacement."""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_multiple_spaces():
    """Test replacing multiple spaces."""
    assert replace_spaces_with_underscores("  spaces  around  ") == "__spaces__around__"

def test_replace_empty_string():
    """Test replacing spaces in an empty string."""
    assert replace_spaces_with_underscores("") == ""

def test_replace_no_spaces():
    """Test string with no spaces."""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_spaces_with_underscores(123)
        replace_spaces_with_underscores(None)
        replace_spaces_with_underscores(["list"])