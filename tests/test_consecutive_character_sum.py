import pytest
from src.consecutive_character_sum import max_consecutive_character_sum

def test_basic_consecutive_characters():
    assert max_consecutive_character_sum("abcdef") == 621  # a(97) + b(98) + c(99) + d(100) + e(101) + f(102)

def test_mixed_consecutive_characters():
    assert max_consecutive_character_sum("acdefg") == 413  # a(97) + c(99) + d(100) + e(101) + f(102) + g(103)

def test_empty_string():
    assert max_consecutive_character_sum("") == 0

def test_single_character():
    assert max_consecutive_character_sum("z") == 122  # z(122)

def test_no_consecutive_characters():
    assert max_consecutive_character_sum("bdhjl") == 106  # Highest single character value

def test_repeated_consecutive_sequences():
    assert max_consecutive_character_sum("abcdabcdefg") == 621  # max of abcdef or cdefg

def test_case_sensitivity():
    assert max_consecutive_character_sum("aAaA") == max(97, 65)  # Treat lowercase and uppercase differently