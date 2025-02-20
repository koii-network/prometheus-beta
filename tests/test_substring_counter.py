import pytest
from src.substring_counter import count_substring_occurrences

def test_basic_substring_count():
    assert count_substring_occurrences("hello hello world", "hello") == 2
    assert count_substring_occurrences("banana", "ana") == 1
    assert count_substring_occurrences("mississippi", "iss") == 2

def test_no_occurrences():
    assert count_substring_occurrences("hello world", "xyz") == 0

def test_overlapping_substrings():
    assert count_substring_occurrences("aaaaa", "aa") == 4

def test_single_character_substring():
    assert count_substring_occurrences("hello world", "l") == 3

def test_entire_string_as_substring():
    assert count_substring_occurrences("hello", "hello") == 1

def test_empty_input_raises_error():
    with pytest.raises(ValueError):
        count_substring_occurrences("", "test")
    
    with pytest.raises(ValueError):
        count_substring_occurrences("test", "")

def test_substring_longer_than_main_string():
    assert count_substring_occurrences("abc", "abcd") == 0