import pytest
from src.string_utils import longest_common_prefix

def test_common_prefix_multiple_strings():
    """Test common prefix for multiple strings with a shared prefix."""
    strings = ["flower", "flow", "flight"]
    assert longest_common_prefix(strings) == "fl"

def test_common_prefix_single_string():
    """Test when only one string is present."""
    strings = ["hello"]
    assert longest_common_prefix(strings) == "hello"

def test_common_prefix_no_common_prefix():
    """Test when no common prefix exists."""
    strings = ["dog", "racecar", "car"]
    assert longest_common_prefix(strings) == ""

def test_common_prefix_empty_strings():
    """Test with empty strings."""
    strings = ["", "b"]
    assert longest_common_prefix(strings) == ""

def test_common_prefix_same_strings():
    """Test when all strings are identical."""
    strings = ["python", "python", "python"]
    assert longest_common_prefix(strings) == "python"

def test_invalid_input_types():
    """Test invalid input types raise TypeError."""
    with pytest.raises(TypeError):
        longest_common_prefix("not a list")
    with pytest.raises(TypeError):
        longest_common_prefix(123)

def test_empty_list():
    """Test that empty list raises ValueError."""
    with pytest.raises(ValueError):
        longest_common_prefix([])