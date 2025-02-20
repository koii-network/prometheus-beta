import pytest
from src.longest_common_substring import longest_common_substring

def test_common_substring_basic():
    assert longest_common_substring("hello", "world") == "l"
    
def test_common_substring_multiple():
    assert longest_common_substring("abcdef", "abcxyz") == "abc"
    
def test_common_substring_full_match():
    assert longest_common_substring("python", "python") == "python"
    
def test_common_substring_no_match():
    assert longest_common_substring("abc", "xyz") == ""
    
def test_common_substring_empty_strings():
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("abc", "") == ""
    assert longest_common_substring("", "xyz") == ""
    
def test_common_substring_case_sensitive():
    assert longest_common_substring("Hello", "hello") == ""
    
def test_common_substring_complex():
    assert longest_common_substring("ABABC", "BABCA") == "BABC"
    
def test_common_substring_repeated_chars():
    assert longest_common_substring("aaaaaa", "aaabaa") == "aaaa"