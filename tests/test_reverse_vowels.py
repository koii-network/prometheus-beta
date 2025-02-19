import pytest
from src.reverse_vowels import reverse_vowels_in_substring

def test_reverse_vowels_in_substring_basic():
    assert reverse_vowels_in_substring("hello world", 0, 5) == "hollo werld"
    assert reverse_vowels_in_substring("python programming", 7, 17) == "python pragramming"

def test_reverse_vowels_in_substring_edge_cases():
    # Empty string
    assert reverse_vowels_in_substring("", 0, 0) == ""
    
    # No vowels in substring
    assert reverse_vowels_in_substring("hello world", 6, 11) == "hello world"
    
    # Full string reversal
    assert reverse_vowels_in_substring("hello", 0, 5) == "holle"

def test_reverse_vowels_in_substring_error_handling():
    # Invalid input type
    with pytest.raises(TypeError):
        reverse_vowels_in_substring(123, 0, 3)
    
    # Invalid indices
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", -1, 6)
    
    with pytest.raises(ValueError):
        reverse_vowels_in_substring("hello", 3, 2)

def test_reverse_vowels_in_substring_mixed_case():
    assert reverse_vowels_in_substring("Hello World", 0, 5) == "Hollo Werld"

def test_reverse_vowels_in_substring_complex():
    assert reverse_vowels_in_substring("abcdefghijklmnopqrstuvwxyz", 10, 20) == "abcdefghijOqnmrpstuvwxyz"