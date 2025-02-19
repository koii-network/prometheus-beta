import pytest
from src.substring_generator import get_all_substrings

def test_normal_string_substrings():
    """Test substring generation for a normal string."""
    result = get_all_substrings("abc")
    assert sorted(result) == sorted(['a', 'ab', 'abc', 'b', 'bc', 'c'])
    assert len(result) == 6

def test_empty_string():
    """Test substring generation for an empty string."""
    result = get_all_substrings("")
    assert result == []

def test_single_character_string():
    """Test substring generation for a single character string."""
    result = get_all_substrings("x")
    assert result == ['x']

def test_repeated_characters_string():
    """Test substring generation for a string with repeated characters."""
    result = get_all_substrings("aaa")
    assert sorted(result) == sorted(['a', 'a', 'a', 'aa', 'aa', 'aaa'])
    assert len(result) == 6

def test_invalid_input_type():
    """Test error handling for non-string input."""
    with pytest.raises(TypeError, match="Input must be a string"):
        get_all_substrings(123)
    with pytest.raises(TypeError, match="Input must be a string"):
        get_all_substrings(None)

def test_special_characters_string():
    """Test substring generation for a string with special characters."""
    result = get_all_substrings("!@#")
    assert sorted(result) == sorted(['!', '!@', '!@#', '@', '@#', '#'])
    assert len(result) == 6