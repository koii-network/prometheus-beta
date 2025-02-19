import pytest
from src.substring_counter import count_distinct_substrings

def test_empty_string():
    assert count_distinct_substrings("") == 1

def test_single_character():
    assert count_distinct_substrings("a") == 2

def test_repeated_characters():
    assert count_distinct_substrings("aaa") == 4

def test_unique_characters():
    assert count_distinct_substrings("abcde") == 16

def test_mixed_string():
    assert count_distinct_substrings("banana") == 16

def test_null_input():
    with pytest.raises(TypeError):
        count_distinct_substrings(None)

def test_various_cases():
    test_cases = [
        ("", 1),
        ("a", 2),
        ("aa", 4),
        ("abc", 10),
        ("banana", 16)
    ]
    
    for input_str, expected_count in test_cases:
        assert count_distinct_substrings(input_str) == expected_count