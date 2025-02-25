import pytest
from src.string_utils import find_longest_common_suffix

def test_common_suffix_basic():
    """Test finding a common suffix in multiple strings."""
    assert find_longest_common_suffix(["flower", "power", "tower"]) == "ower"

def test_common_suffix_single_char():
    """Test finding a single character common suffix."""
    assert find_longest_common_suffix(["cat", "bat", "rat"]) == "at"

def test_common_suffix_full_string_match():
    """Test when the entire string is a suffix."""
    assert find_longest_common_suffix(["hello", "hello"]) == "hello"

def test_empty_list():
    """Test behavior with an empty list."""
    assert find_longest_common_suffix([]) == ""

def test_single_string():
    """Test behavior with a single string."""
    assert find_longest_common_suffix(["python"]) == "python"

def test_no_common_suffix():
    """Test when there is no common suffix."""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_different_length_strings():
    """Test with strings of different lengths."""
    assert find_longest_common_suffix(["longer", "short"]) == ""

def test_invalid_input_type():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_list_contents():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["valid", 123, "strings"])

def test_empty_string_list():
    """Test behavior with a list of empty strings."""
    assert find_longest_common_suffix(["", "", ""]) == ""