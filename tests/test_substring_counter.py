import pytest
from src.substring_counter import count_substring_occurrences

def test_basic_substring_count():
    assert count_substring_occurrences("hello hello world", "hello") == 2
    assert count_substring_occurrences("banana", "ana") == 1
    assert count_substring_occurrences("mississippi", "iss") == 2

def test_no_substring_matches():
    assert count_substring_occurrences("hello world", "python") == 0
    assert count_substring_occurrences("abcdef", "xyz") == 0

def test_substring_at_start_and_end():
    assert count_substring_occurrences("hellohellohello", "hello") == 3

def test_overlapping_substrings():
    assert count_substring_occurrences("aaaaa", "aa") == 4

def test_single_character_substring():
    assert count_substring_occurrences("hello world", "l") == 3

def test_full_string_as_substring():
    assert count_substring_occurrences("hello", "hello") == 1
    assert count_substring_occurrences("hello", "Hello") == 0  # Case-sensitive

def test_empty_or_none_inputs():
    with pytest.raises(ValueError, match="Substring cannot be empty"):
        count_substring_occurrences("hello", "")
    
    with pytest.raises(TypeError, match="Both string and substring must be strings"):
        count_substring_occurrences(None, "hello")
    
    with pytest.raises(TypeError, match="Both string and substring must be strings"):
        count_substring_occurrences("hello", None)

def test_substring_longer_than_string():
    assert count_substring_occurrences("hi", "hello") == 0