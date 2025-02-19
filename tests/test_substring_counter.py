import pytest
from src.substring_counter import count_distinct_substrings

def test_distinct_substrings_empty_string():
    assert count_distinct_substrings("") == 0

def test_distinct_substrings_single_char():
    assert count_distinct_substrings("a") == 1

def test_distinct_substrings_repeated_chars():
    assert count_distinct_substrings("aaaa") == 1

def test_distinct_substrings_unique_chars():
    assert count_distinct_substrings("abcde") == 15

def test_distinct_substrings_mixed_repetition():
    assert count_distinct_substrings("banana") == 15

def test_distinct_substrings_complex_string():
    assert count_distinct_substrings("ABABC") == 13

def test_distinct_substrings_case_sensitive():
    result = count_distinct_substrings("AbA")
    assert result == 4  # Substrings: "", "A", "b", "Ab", "bA", "AbA"