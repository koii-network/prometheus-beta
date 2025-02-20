import pytest
from src.unique_chars import count_unique_characters

def test_basic_unique_characters():
    assert count_unique_characters("hello") == 4
    assert count_unique_characters("programming") == 8

def test_case_sensitivity():
    assert count_unique_characters("aAaA") == 2  # 'a' and 'A' are different
    assert count_unique_characters("AbCdEfG") == 7

def test_edge_cases():
    assert count_unique_characters("") == 0  # Empty string
    assert count_unique_characters("   ") == 1  # Whitespace string
    assert count_unique_characters(None) == 0  # None input

def test_repeated_characters():
    assert count_unique_characters("aaaaaa") == 1
    assert count_unique_characters("abcabcabc") == 3

def test_special_characters():
    assert count_unique_characters("!@#$%^&*()") == 10
    assert count_unique_characters("Hello, World!") == 10  # Mix of characters