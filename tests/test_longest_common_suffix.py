import pytest
from src.longest_common_suffix import find_longest_common_suffix

def test_multiple_strings_with_common_suffix():
    """Test finding common suffix with multiple strings."""
    assert find_longest_common_suffix(["flower", "tower", "shower"]) == "wer"

def test_single_string():
    """Test behavior with a single string."""
    assert find_longest_common_suffix(["hello"]) == "hello"

def test_no_common_suffix():
    """Test when no common suffix exists."""
    assert find_longest_common_suffix(["abc", "def", "ghi"]) == ""

def test_empty_list():
    """Test with an empty list."""
    assert find_longest_common_suffix([]) == ""

def test_strings_different_lengths():
    """Test with strings of different lengths."""
    assert find_longest_common_suffix(["color", "color", "col"]) == ""

def test_edge_case_identical_strings():
    """Test with identical strings."""
    assert find_longest_common_suffix(["hello", "hello", "hello"]) == "hello"

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_suffix("not a list")

def test_invalid_input_non_string_elements():
    """Test raising TypeError for non-string list elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_suffix(["valid", 123, "also valid"])