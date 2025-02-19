import pytest
from src.distinct_substrings import count_distinct_substrings

def test_distinct_substrings_basic():
    assert count_distinct_substrings('aab') == 6
    assert count_distinct_substrings('abcde') == 15

def test_distinct_substrings_empty_string():
    assert count_distinct_substrings('') == 0

def test_distinct_substrings_single_char():
    assert count_distinct_substrings('a') == 1

def test_distinct_substrings_repeated_chars():
    assert count_distinct_substrings('aaaa') == 4

def test_distinct_substrings_complex():
    assert count_distinct_substrings('banana') == 15

def test_distinct_substrings_special_chars():
    assert count_distinct_substrings('!@#') == 6

def test_distinct_substrings_mixed_case():
    assert count_distinct_substrings('AbCa') == 10