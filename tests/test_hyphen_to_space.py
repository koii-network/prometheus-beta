import pytest
from src.hyphen_to_space import replace_hyphens

def test_basic_hyphen_replacement():
    """Test basic hyphen replacement."""
    assert replace_hyphens("hello-world") == "hello world"

def test_multiple_hyphens():
    """Test replacing multiple hyphens."""
    assert replace_hyphens("python-is-awesome") == "python is awesome"

def test_no_hyphens():
    """Test string with no hyphens remains unchanged."""
    assert replace_hyphens("pythonisawesome") == "pythonisawesome"

def test_empty_string():
    """Test empty string handling."""
    assert replace_hyphens("") == ""

def test_string_with_spaces():
    """Test handling of string that already contains spaces."""
    assert replace_hyphens("python-is awesome") == "python is awesome"

def test_type_error():
    """Test that TypeError is raised for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        replace_hyphens(123)
        replace_hyphens(None)
        replace_hyphens(["hello-world"])