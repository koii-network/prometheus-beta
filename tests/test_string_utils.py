import pytest
from src.string_utils import replace_spaces_with_underscores

def test_replace_spaces_with_underscores_basic():
    """Test basic space replacement"""
    assert replace_spaces_with_underscores("hello world") == "hello_world"

def test_replace_spaces_with_underscores_multiple_spaces():
    """Test replacement with multiple spaces"""
    assert replace_spaces_with_underscores("hello  world") == "hello__world"

def test_replace_spaces_with_underscores_leading_trailing_spaces():
    """Test replacement with leading and trailing spaces"""
    assert replace_spaces_with_underscores("  hello world  ") == "__hello_world__"

def test_replace_spaces_with_underscores_empty_string():
    """Test with empty string"""
    assert replace_spaces_with_underscores("") == ""

def test_replace_spaces_with_underscores_no_spaces():
    """Test string with no spaces"""
    assert replace_spaces_with_underscores("helloworld") == "helloworld"

def test_replace_spaces_with_underscores_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(123)
    with pytest.raises(TypeError):
        replace_spaces_with_underscores(None)