import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_multiple_strings_with_common_prefix():
    """Test finding common prefix with multiple strings."""
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_single_string():
    """Test with a single string."""
    assert find_longest_common_prefix(["alone"]) == "alone"

def test_empty_list():
    """Test with an empty list."""
    assert find_longest_common_prefix([]) == ""

def test_no_common_prefix():
    """Test strings with no common prefix."""
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_all_strings_identical():
    """Test when all strings are identical."""
    assert find_longest_common_prefix(["hello", "hello", "hello"]) == "hello"

def test_different_string_lengths():
    """Test strings of different lengths."""
    assert find_longest_common_prefix(["abc", "abcd", "ab"]) == "ab"

def test_invalid_input_non_list():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list of strings"):
        find_longest_common_prefix("not a list")

def test_invalid_input_non_string_elements():
    """Test raising TypeError for list with non-string elements."""
    with pytest.raises(TypeError, match="All elements must be strings"):
        find_longest_common_prefix(["valid", 123, "invalid"])

def test_unicode_strings():
    """Test with Unicode strings."""
    assert find_longest_common_prefix(["café", "cafè", "cafë"]) == "caf"