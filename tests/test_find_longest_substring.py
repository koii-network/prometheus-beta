import pytest
from src.find_longest_substring import find_longest_substring

def test_find_longest_substring_basic():
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_find_longest_substring_edge_cases():
    assert find_longest_substring("") == ""
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aab") == "ab"

def test_find_longest_substring_complex():
    assert find_longest_substring("dvdf") == "vdf"
    assert find_longest_substring("tmmzuxt") == "mzuxt"
    
def test_find_longest_substring_mixed_case():
    assert find_longest_substring("AbCdEfG") == "AbCdEfG"
    assert find_longest_substring("aAbBcC") == "aAbB"