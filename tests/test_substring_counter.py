import pytest
from src.substring_counter import count_substring_occurrences

def test_basic_substring_counting():
    assert count_substring_occurrences("hello hello world", "hello") == 2
    assert count_substring_occurrences("mississippi", "iss") == 2
    assert count_substring_occurrences("aaa", "aa") == 2

def test_no_occurrences():
    assert count_substring_occurrences("hello world", "xyz") == 0
    assert count_substring_occurrences("hello", "hello world") == 0

def test_overlapping_substrings():
    assert count_substring_occurrences("aaaaa", "aa") == 4

def test_single_character_substring():
    assert count_substring_occurrences("hello", "l") == 2

def test_empty_main_string():
    assert count_substring_occurrences("", "test") == 0

def test_invalid_inputs():
    with pytest.raises(ValueError, match="Inputs cannot be None"):
        count_substring_occurrences(None, "test")
    with pytest.raises(ValueError, match="Inputs cannot be None"):
        count_substring_occurrences("test", None)
    with pytest.raises(ValueError, match="Substring cannot be empty"):
        count_substring_occurrences("test", "")