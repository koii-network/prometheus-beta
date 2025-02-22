import pytest
from src.remove_excess_duplicates import remove_excess_duplicates

def test_remove_excess_duplicates_basic():
    # Basic case with duplicates more than twice
    assert remove_excess_duplicates("aabbcccd") == "aabbcc"

def test_remove_excess_duplicates_no_change():
    # String with no more than two duplicates of any character
    assert remove_excess_duplicates("abcde") == "abcde"

def test_remove_excess_duplicates_multiple_chars():
    # Multiple characters with different duplicate counts
    assert remove_excess_duplicates("aaabbbccccdddeee") == "aabbccddee"

def test_remove_excess_duplicates_empty_string():
    # Empty string case
    assert remove_excess_duplicates("") == ""

def test_remove_excess_duplicates_invalid_input():
    # Invalid input type
    with pytest.raises(TypeError):
        remove_excess_duplicates(123)

def test_remove_excess_duplicates_special_chars():
    # Test with special characters and mixed cases
    assert remove_excess_duplicates("!!@@##$$$%%") == "!!@@##$$%"