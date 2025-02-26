import pytest
from src.substring_counter import count_substring_occurrences

def test_basic_substring_counting():
    """Test basic substring counting scenarios."""
    assert count_substring_occurrences("hello hello world", "hello") == 2
    assert count_substring_occurrences("aaaaa", "aa") == 2
    assert count_substring_occurrences("mississippi", "iss") == 2
    assert count_substring_occurrences("python programming", "python") == 1

def test_no_occurrences():
    """Test scenarios with no substring occurrences."""
    assert count_substring_occurrences("hello world", "python") == 0
    assert count_substring_occurrences("", "test") == 0

def test_substring_longer_than_text():
    """Test when substring is longer than the text."""
    assert count_substring_occurrences("short", "longer substring") == 0

def test_empty_substring():
    """Test raising ValueError for empty substring."""
    with pytest.raises(ValueError, match="Substring cannot be empty"):
        count_substring_occurrences("hello", "")

def test_type_errors():
    """Test raising TypeError for non-string inputs."""
    with pytest.raises(TypeError, match="Both text and substring must be strings"):
        count_substring_occurrences(123, "test")
    with pytest.raises(TypeError, match="Both text and substring must be strings"):
        count_substring_occurrences("hello", 123)

def test_case_sensitivity():
    """Test case-sensitive substring counting."""
    assert count_substring_occurrences("Hello HELLO hello", "hello") == 1
    assert count_substring_occurrences("Hello HELLO hello", "Hello") == 1

def test_single_character_substring():
    """Test counting single character substrings."""
    assert count_substring_occurrences("aaaaaa", "a") == 6
    assert count_substring_occurrences("abracadabra", "a") == 5

def test_edge_cases():
    """Test various edge case scenarios."""
    assert count_substring_occurrences(" ", " ") == 1
    assert count_substring_occurrences("x", "x") == 1
    assert count_substring_occurrences("", "") == 0  # unique edge case