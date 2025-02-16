import pytest
from src.string_utils import longest_common_prefix

def test_basic_common_prefix():
    """Test finding common prefix in a list of strings."""
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"

def test_no_common_prefix():
    """Test case with no common prefix."""
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_string():
    """Test with a single string input."""
    assert longest_common_prefix(["alone"]) == "alone"

def test_empty_list():
    """Test with an empty list."""
    assert longest_common_prefix([]) == ""

def test_all_same_string():
    """Test with identical strings."""
    assert longest_common_prefix(["abc", "abc", "abc"]) == "abc"

def test_type_error():
    """Test that TypeError is raised for non-string inputs."""
    with pytest.raises(TypeError):
        longest_common_prefix([1, 2, 3])

def test_mixed_case_prefix():
    """Test case sensitivity in prefix."""
    assert longest_common_prefix(["Apple", "App", "Applications"]) == "App"

def test_unicode_strings():
    """Test with unicode strings."""
    assert longest_common_prefix(["café", "cafeteria", "cafè"]) == "caf"

def test_whitespace_prefix():
    """Test with strings having whitespace prefix."""
    assert longest_common_prefix(["  hello", "  world", "  test"]) == "  "