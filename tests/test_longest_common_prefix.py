import pytest
from src.longest_common_prefix import find_longest_common_prefix

def test_normal_common_prefix():
    """Test finding a common prefix in normal scenarios."""
    assert find_longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert find_longest_common_prefix(["dog", "racecar", "car"]) == ""

def test_single_string():
    """Test behavior with a single string."""
    assert find_longest_common_prefix(["alone"]) == "alone"

def test_empty_list():
    """Test behavior with an empty list."""
    assert find_longest_common_prefix([]) == ""

def test_identical_strings():
    """Test with identical strings."""
    assert find_longest_common_prefix(["abc", "abc", "abc"]) == "abc"

def test_prefix_is_full_string():
    """Test when prefix is a full string."""
    assert find_longest_common_prefix(["a", "ab", "abc"]) == "a"

def test_invalid_input_types():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        find_longest_common_prefix(None)
    
    with pytest.raises(TypeError):
        find_longest_common_prefix([1, 2, 3])
    
    with pytest.raises(TypeError):
        find_longest_common_prefix(["valid", 123, "strings"])

def test_unicode_strings():
    """Test with Unicode strings."""
    assert find_longest_common_prefix(["café", "cafè", "cafë"]) == "caf"