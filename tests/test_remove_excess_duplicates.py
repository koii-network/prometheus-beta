import pytest
from src.remove_excess_duplicates import remove_excess_duplicates

def test_remove_excess_duplicates_standard_cases():
    """Test standard cases of excess duplicate removal."""
    assert remove_excess_duplicates("aabbbcccc") == "aabbcc"
    assert remove_excess_duplicates("aaabbbccc") == "aabbcc"
    assert remove_excess_duplicates("hello") == "hello"

def test_remove_excess_duplicates_edge_cases():
    """Test edge cases of the function."""
    assert remove_excess_duplicates("") == ""
    assert remove_excess_duplicates("a") == "a"
    assert remove_excess_duplicates("aa") == "aa"

def test_remove_excess_duplicates_complex_cases():
    """Test more complex string scenarios."""
    assert remove_excess_duplicates("aaaaabbbbbccccc") == "aabbcc"
    assert remove_excess_duplicates("abcdefg") == "abcdefg"
    assert remove_excess_duplicates("aaabbbcccddd") == "aabbccdd"

def test_remove_excess_duplicates_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        remove_excess_duplicates(123)
    with pytest.raises(TypeError):
        remove_excess_duplicates(None)

def test_remove_excess_duplicates_mixed_case():
    """Test cases with mixed character cases."""
    assert remove_excess_duplicates("AAAbbbCCCc") == "AAbbCCc"